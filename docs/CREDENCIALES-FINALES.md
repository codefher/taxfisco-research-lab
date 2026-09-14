# Credenciales Finales - TaxFisco Research Lab

## IMPORTANTE
Todas las credenciales se unificaron a Admin1234! para facilitar el acceso.
En produccion, cambialas usando el script scripts/generate-secure-env.sh.

## Servicios principales

- Wazuh Dashboard: https://localhost:1443 - admin / Admin1234!
- Wazuh Indexer (interno): https://wazuh.indexer:9200 - admin / Admin1234!
- Wazuh Indexer Proxy (host): http://localhost:19200 - admin / Admin1234!
- Wazuh Manager API: https://wazuh.manager:55000 - wazuh-wui / wazuh-wui
- TheHive: http://localhost:9000 - admin@thehive.local / secret
- MISP: https://localhost:8443 - admin@admin.test / Admin1234!
- MISP API Key: 6fcc1596efd99309d126409a558cf2d9
- Cortex: http://localhost:9001 - (configurar en primer login)
- Shuffle: http://localhost:3001 - (registrarse en primer login)
- Grafana: http://localhost:3000 - admin / Admin1234!
- Velociraptor: https://localhost:8889 - admin / Admin1234!
- Decoy API: http://localhost:8090 - admin / admin
- Decoy Portal: http://localhost:8890 - admin / admin

## Bases de datos

- Postgres fiscal: fiscal / Admin1234!
- MISP DB: misp / Admin1234!
- Shuffle DB: shuffle / Admin1234!

## Honeypots

- Cowrie SSH: localhost:2222 - root / cualquiera
- Cowrie Telnet: localhost:2223 - root / cualquiera
- OpenCanary FTP: localhost:2121 - cualquiera
- OpenCanary SSH: localhost:2223 - cualquiera
- OpenCanary HTTP: localhost:8081
- Heralding Telnet: localhost:23 - cualquiera

## Comandos utiles

    bash scripts/verify-services.sh
    
    docker compose exec attacker bash
    
    docker compose exec attacker bash /root/attack-scenarios/run_all.sh
    
    docker compose exec attacker bash /root/attack-scenarios/S04-sql-injection/ejecutar.sh
    
    docker compose logs -f wazuh.manager
    
    docker compose down && docker compose up -d
    
    make backup

## Cambios aplicados en esta sesion

1. Certificados SSL regenerados con SAN para los nombres de servicio
2. Password admin del indexer cambiado a Admin1234!
3. Modo compatibilidad filebeat/OpenSearch activado
4. Wazuh Dashboard con config custom y keystore correcto
5. TheHive con indice thehive_global y password actualizado
6. MISP con Redis, DB inicializada, admin user y API key
7. Shuffle con credenciales de OpenSearch actualizadas
8. Decoy Portal con migraciones y superuser
9. Attacker con volumenes rw y herramientas instaladas
