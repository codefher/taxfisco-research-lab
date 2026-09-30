# Acceso a los servicios — Prototipo II (SIN)

Todos los servicios del laboratorio están operativos. Este documento reúne
las direcciones y credenciales para acceder a cada uno desde el equipo
anfitrión.

> Los certificados son autofirmados: el navegador pedirá aceptar la
> excepción de seguridad la primera vez. Es esperado en un laboratorio.

## Servicios web

| Servicio | Dirección | Usuario | Contraseña |
|---|---|---|---|
| Portal del contribuyente | http://localhost:8890 | `1020304050` | `Prueba2024!` |
| Portal (administración Django) | http://localhost:8890/admin/ | `admin` | `admin` |
| API de Servicios Tributarios | http://localhost:8090/docs | — | — |
| Grafana | http://localhost:3000 | `admin` | `Admin1234!` |
| MISP | https://localhost:8443 | `admin@admin.test` | `Admin1234!` |
| TheHive | http://localhost:9000 | `admin@thehive.local` | `secret` |
| Cortex | http://localhost:9001 | `admin` | `Admin1234!` |
| Shuffle | http://localhost:3001 | `admin` | `Shuffle_Admin_2024!` |
| Wazuh Dashboard | https://localhost:1443 | `admin` | `admin` |
| Velociraptor | https://localhost:8889 | `admin` | `Admin1234!` |

> **Velociraptor** usa autenticación HTTP Basic: al abrir la URL el
> navegador pedirá usuario y contraseña. Los comandos de API requieren
> además el encabezado `Referer`, por lo que conviene usar la interfaz
> web en lugar de `curl` para las operaciones.

## API de MISP

La clave de API se generó durante el aprovisionamiento y quedó registrada
en la tabla `auth_keys` de la base de MISP. Para consultarla:

```bash
docker exec sin-misp-db mysql -u root -p"$MISP_DB_ROOT_PASSWORD" misp \
  -N -e "SELECT authkey FROM auth_keys WHERE user_id=1;"
```

## Notas de configuración

Cada servicio que reutiliza el índice de Wazuh se conecta por el proxy
`wazuh-indexer-proxy:9200`, que exige autenticación básica con las
credenciales del administrador del índice (`admin` / `admin`).

- **TheHive** y **Cortex** usan índices dedicados (`thehive`, `cortex_6`)
  sobre el mismo índice de Wazuh.
- **Shuffle** usa el índice para su almacén de organizaciones y datos.
- La contraseña del índice es `admin` porque es la que deja el proceso
  `securityadmin -icl` al inicializar desde la imagen de Wazuh.

## Verificación

```bash
python3 /tmp/sin-ref/verificar.py
```

Comprueba el acceso a los nueve servicios y reporta cuáles responden.
