# Acceso a los servicios — Prototipo II (SIN)

Todos los servicios del laboratorio están operativos. Este documento reúne
las direcciones y credenciales para acceder a cada uno desde el equipo
anfitrión.

> Credenciales verificadas en ejecución real el 2026-10-04 (login web o API
> de cada servicio).

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
| Shuffle | http://localhost:3001 | `admin@shuffle.local` | `Shuffle_Admin_2024!` |
| Wazuh Dashboard | https://localhost:1443 | `admin` | `admin` |
| Wazuh Indexer | https://localhost:9200 | `admin` | `admin` |
| Velociraptor | https://localhost:8889 | `admin` | `Admin1234!` |

> **Velociraptor** usa autenticación HTTP Basic: al abrir la URL el
> navegador pedirá usuario y contraseña. Los comandos de API requieren
> además el encabezado `Referer`, por lo que conviene usar la interfaz
> web en lugar de `curl` para las operaciones.
>
> Si se reinician los volúmenes del contenedor, el usuario administrador
> debe recrearse (el config montado en `docker-compose.yml` impide que la
> imagen lo genere sola):
>
> ```bash
> make velociraptor-setup
> ```

> **Shuffle** mostrará la pantalla de configuración inicial la primera vez
> (`/adminsetup`): se registra ahí el usuario `admin@shuffle.local` con la
> contraseña de la tabla y luego se accede por `/login`.

> **MISP**: el acceso web usa las credenciales de la tabla. MISP 2.4.177
> usa *advanced authkeys*: la clave legacy de la tabla `users` es ignorada.
> La clave de API vigente (creada 2026-10-04, tabla `auth_keys`) es:
>
> ```
> RaKjZFkdXuoXYPIaAJfzOpTj9lAPw4vJNGXm4k5e
> ```
>
> ```bash
> curl -sk -H "Authorization: RaKjZFkdXuoXYPIaAJfzOpTj9lAPw4vJNGXm4k5e" \
>   -H "Accept: application/json" https://localhost:8443/users/view/me
> ```
>
> Si se pierde, generar una nueva desde *Administration → Auth Keys*.

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
