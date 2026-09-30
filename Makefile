# SIN Research Lab - Makefile (16 GB RAM Profile)
# Simplifica las operaciones comunes del laboratorio principal
#
# Este es el perfil LITE principal del laboratorio, optimizado para
# correr en workstations con 16 GB de RAM + 8 GB de swap.
#
# Características:
# - Comandos lite-* con setup de swap automático
# - Servicio thehive.es eliminado (reutiliza wazuh.indexer)
# - Mem_limits reducidos en 23 servicios
# - Misma cobertura funcional y académica que la versión sin restricciones
#
# Si en el futuro amplías a 32 GB de RAM, ver: ../lab-1/Makefile (opcional)

.PHONY: help install up down restart logs ps status \
        lite-up lite-down lite-status lite-clean \
        build attacker exec clean backup restore test \
        attacks analysis dashboards \
        swap-setup thehive-setup

help:
	@echo "SIN Research Lab - LITE EDITION (16 GB) - Comandos disponibles:"
	@echo ""
	@echo "  Instalación (perfil lite):"
	@echo "    make install         - Configurar entorno (.env)"
	@echo "    make lite-up         - Levantar lab + crear swap + configurar TheHive"
	@echo "    make lite-down       - Detener lab"
	@echo "    make lite-status     - Estado + uso de RAM"
	@echo "    make lite-clean      - Limpiar todo (incluye datos)"
	@echo ""
	@echo "  Monitoreo:"
	@echo "    make ps              - Listar servicios activos"
	@echo "    make logs            - Ver logs en tiempo real"
	@echo "    make status          - Health checks"
	@echo "    make stats           - Uso de recursos (CPU/RAM)"
	@echo ""
	@echo "  Ataques:"
	@echo "    make attacks         - Ejecutar los 10 escenarios"
	@echo "    make analysis        - Generar análisis de KPIs"
	@echo "    make S04             - Ejecutar escenario individual (S01..S10)"
	@echo ""
	@echo "  Mantenimiento:"
	@echo "    make swap-setup      - Crear/verificar 8 GB de swap"
	@echo "    make thehive-setup   - Crear índice TheHive en Wazuh Indexer"
	@echo "    make clean           - Detener y borrar volúmenes"
	@echo "    make backup          - Backup de datos"
	@echo ""
	@echo "  Acceso:"
	@echo "    make attacker        - Acceder al contenedor atacante"
	@echo "    make dashboards      - Ver URLs de todos los dashboards"

install:
	@echo "=== Configurando entorno ==="
	@if [ ! -f .env ]; then cp .env.example .env && echo "[OK] .env creado. Edítalo antes de continuar."; else echo "[OK] .env ya existe"; fi
	@echo "Edita .env con tus contraseñas: nano .env"
	@echo ""
	@echo "IMPORTANTE: Este perfil requiere mínimo 16 GB de RAM."
	@echo "Si tienes menos, considera usar lab-1/ con --scale=0 para algunos servicios."

lite-up: swap-setup
	@echo "=== Levantando servicios (perfil lite 16 GB) ==="
	docker compose up -d
	@echo ""
	@echo "[OK] Servicios iniciados. Esperando 90 segundos para estabilización..."
	@sleep 90
	@echo ""
	@echo "=== Configurando índice TheHive en Wazuh Indexer ==="
	@$(MAKE) thehive-setup
	@echo ""
	@$(MAKE) lite-status

lite-down:
	@echo "=== Deteniendo servicios ==="
	docker compose down

lite-status:
	@echo "=== Estado del lab ==="
	@docker compose ps
	@echo ""
	@echo "=== Uso de RAM por contenedor ==="
	@docker stats --no-stream
	@echo ""
	@echo "=== Tips para 16 GB ==="
	@echo "  • Cierra Chrome/Firefox cuando ejecutes escenarios pesados (S08, S10)"
	@echo "  • No abras más de 2 dashboards a la vez"
	@echo "  • Ejecuta escenarios uno por uno (no en paralelo)"
	@echo "  • TheHive y Cortex ahora usan el ES de Wazuh (índice dedicado)"
	@echo "  • Si ves OOM kill, ejecuta: docker compose restart wazuh.indexer"

lite-clean:
	@echo "=== ADVERTENCIA: Esto borrará TODOS los datos del lab ==="
	@echo "Presiona Ctrl+C en 5 segundos para cancelar..."
	@sleep 5
	docker compose down -v
	docker system prune -af
	@echo "[OK] Lab limpio. Ejecuta 'make lite-up' para reiniciar."

swap-setup:
	@echo "=== Verificando swap ==="
	@if [ "$$(swapon --show | wc -l)" -lt 2 ]; then \
		echo "Creando 8 GB de swap..."; \
		bash scripts/setup-swap-8gb.sh; \
	else \
		echo "[OK] Swap ya configurado:"; \
		swapon --show; \
	fi

thehive-setup:
	@echo "=== Configurando índice TheHive en Wazuh Indexer ==="
	@bash scripts/setup-wazuh-index-for-thehive.sh

up:
	@echo "=== NOTA: usa 'make lite-up' para el perfil de 16 GB ==="
	@echo "=== Continuando con docker compose up... ==="
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

ps:
	@echo "=== Servicios activos ==="
	docker compose ps

logs:
	docker compose logs -f --tail=100

status:
	@echo "=== Health checks ==="
	@for svc in wazuh.manager wazuh.dashboard thehive misp.core shuffle velociraptor grafana decoy.api; do \
		state=$$(docker inspect --format='{{.State.Health.Status}}' sin-$$svc 2>/dev/null || echo "no-healthcheck"); \
		echo "  $$svc: $$state"; \
	done

stats:
	docker stats --no-stream

attacks:
	@echo "=== Ejecutando los 10 escenarios de ataque ==="
	docker compose exec attacker bash /root/attack-scenarios/run_all.sh

analysis:
	@echo "=== Generando análisis de KPIs (datos reales) ==="
	KPI_OUTPUT=evidencias/07-metricas/07_kpi-report.json python3 analysis/kpi_calculator.py
	docker compose exec attacker python3 /root/analysis/mitre_coverage.py
	docker compose exec attacker python3 /root/analysis/iso27035_mapping.py

S01:
	docker compose exec attacker bash /root/attack-scenarios/S01-reconocimiento/ejecutar.sh
S02:
	docker compose exec attacker bash /root/attack-scenarios/S02-escaneo-web/ejecutar.sh
S03:
	docker compose exec attacker bash /root/attack-scenarios/S03-bruteforce-ssh/ejecutar.sh
S04:
	docker compose exec attacker bash /root/attack-scenarios/S04-sql-injection/ejecutar.sh
S05:
	docker compose exec attacker bash /root/attack-scenarios/S05-credential-stuffing/ejecutar.sh
S06:
	docker compose exec attacker bash /root/attack-scenarios/S06-xss/ejecutar.sh
S07:
	docker compose exec attacker bash /root/attack-scenarios/S07-api-abuse/ejecutar.sh
S08:
	docker compose exec attacker bash /root/attack-scenarios/S08-malware-drop/ejecutar.sh
S09:
	docker compose exec attacker bash /root/attack-scenarios/S09-reverse-shell/ejecutar.sh
S10:
	docker compose exec attacker bash /root/attack-scenarios/S10-exfiltracion-dns/ejecutar.sh

attacker:
	docker compose exec attacker bash

dashboards:
	@echo "=== URLs de acceso (perfil lite) ==="
	@echo ""
	@echo "Wazuh Dashboard:    https://localhost:443"
	@echo "  Usuario: admin / (ver docker logs wazuh.manager | grep -i password)"
	@echo ""
	@echo "TheHive:            http://localhost:9000"
	@echo "  Usuario: admin@thehive.local / secret"
	@echo "  NOTA: usa el ES de Wazuh, índice 'thehive'"
	@echo ""
	@echo "MISP:               https://localhost:8443"
	@echo "  Usuario: admin@admin.test / admin"
	@echo ""
	@echo "Shuffle:            http://localhost:3001"
	@echo "Cortex:             http://localhost:9001"
	@echo "  NOTA: usa el ES de Wazuh, índice 'cortex'"
	@echo "Grafana:            http://localhost:3000"
	@echo "  Usuario: admin / (configurado en .env)"
	@echo ""
	@echo "Velociraptor:       https://localhost:8889"
	@echo "Decoy API:          http://localhost:8080"
	@echo "Decoy Portal:       http://localhost:8888"
	@echo ""
	@echo "Cowrie SSH:         ssh -p 2222 root@localhost (cualquier pass)"

clean:
	@echo "=== ADVERTENCIA: Esto borrará TODOS los datos del lab ==="
	@echo "Presiona Ctrl+C en 5 segundos para cancelar..."
	@sleep 5
	docker compose down -v
	docker system prune -af

backup:
	@echo "=== Creando backup de datos ==="
	mkdir -p ./backups/$(shell date +%Y%m%d-%H%M%S)
	@BACKUP_DIR=./backups/$(shell date +%Y%m%d-%H%M%S); \
	mkdir -p $$BACKUP_DIR; \
	docker compose exec -T postgres.fiscal pg_dump -U fiscal sin_fiscal > $$BACKUP_DIR/postgres.sql; \
	docker compose exec -T decoy.api cat /var/log/decoy-api/attacks.json > $$BACKUP_DIR/attacks.json 2>/dev/null || true; \
	tar -czf $$BACKUP_DIR/wazuh-logs.tar.gz -C config/wazuh . 2>/dev/null || true; \
	echo "[OK] Backup guardado en: $$BACKUP_DIR"

restore:
	@echo "=== Restaurar backup ==="
	@ls -la ./backups/

test:
	@echo "=== Tests del Decoy API ==="
	docker compose exec decoy.api python3 -m pytest tests/ -v
