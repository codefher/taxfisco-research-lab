# Correlación con gestión de incidentes — iteración 1 (v2.0-it1)

> **Estado al 2026-10-03: PENDIENTE.**

La correlación con gestión de incidentes requiere que se cree un caso en
TheHive y que Cortex ejecute los analizadores (MISP_2_1 y otros) sobre los
observables del caso. En esta sesión de re-captura de it1:

1. **No se creó caso en TheHive**: el endpoint `POST /api/case` devuelve
   `AuthorizationError: You are not authorized to create case, you don't
   have the permission manageCase/create` para el usuario
   `admin@thehive.local`. Esto es coherente con el hallazgo de la auditoría
   previa y con el estado del rol admin tras los reinicios del lab.

2. **No se ejecutaron jobs de Cortex**: sin caso TheHive, no hay
   observables para enriquecer. El contenedor Cortex responde
   (HTTP 303 / 200) pero la página de Jobs muestra 0 jobs.

3. **MISP conserva 1 evento previo** (ID 1, "SIN - IOCs de la campana de
   ataque observada (escenarios S01-S10)", 8 atributos, 4 ATT&CK
   clusters: T1078, T1105, T1190, T1595) — captura en
   `05-enriquecimiento-custodia/02_misp-evento-iocs.png` y
   `03_misp-evento-detalle.png`. Pero no está enlazado a un caso TheHive
   de esta sesión.

Por tanto, esta subcarpeta queda como PENDIENTE. La captura equivalente
para 4.3.6.5 se completará en la iteración 2 tras:

- añadir el permiso `manageCase/create` al rol admin de TheHive (o crear
  un usuario `caseCreator` dedicado);
- documentar el flujo automático desde una alerta Wazuh (regla 100280)
  hacia un caso TheHive preconfigurado, vía Shuffle SOAR (workflow
  `wazuh-alert-to-thehive`).