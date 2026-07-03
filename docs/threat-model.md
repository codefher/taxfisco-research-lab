# Threat Model - TaxFisco Research Lab

## Modelo STRIDE aplicado al laboratorio

### S - Spoofing
- **Amenaza**: Atacante se hace pasar por usuario legítimo
- **Vector**: Credential stuffing (S05), password guessing (S03)
- **TTPs ATT&CK**: T1110.001, T1110.004
- **Detección**: Wazuh correlación, OpenCanary HTTP honeypot
- **Mitigación**: MFA + rate limiting + WAF

### T - Tampering
- **Amenaza**: Modificación de datos (declaraciones juradas, facturas)
- **Vector**: SQL Injection con mass-assignment (S04, S07)
- **TTPs ATT&CK**: T1190, T1565
- **Detección**: Decoy API attack_logger, FIM Wazuh
- **Mitigación**: Input validation, parametrized queries, audit log

### R - Repudiation
- **Amenaza**: Usuario legítimo niega acciones maliciosas
- **Vector**: Uso de cuentas robadas (S05)
- **TTPs ATT&CK**: T1078
- **Detección**: TheHive case audit log, session tracking
- **Mitigación**: Strong authentication, comprehensive logging

### I - Information Disclosure
- **Amenaza**: Exfiltración de datos confidenciales
- **Vector**: DNS tunneling (S10), IDOR enumeration (S07)
- **TTPs ATT&CK**: T1048.003, T1213, T1530
- **Detección**: Zeek dns.log, Suricata, Wazuh custom rules
- **Mitigación**: DLP, DNS monitoring, field-level encryption

### D - Denial of Service
- **Amenaza**: Interrupción del servicio al contribuyente
- **Vector**: No implementado en el lab (fuera de alcance)
- **TTPs ATT&CK**: T1498, T1499
- **Detección**: Rate limiting en nginx
- **Mitigación**: CDN, WAF, auto-scaling

### E - Elevation of Privilege
- **Amenaza**: Obtener acceso administrativo
- **Vector**: Cookie manipulation (S07), admin endpoint access
- **TTPs ATT&CK**: T1078, T1068
- **Detección**: Decoy API attack_logger, Wazuh 100203
- **Mitigación**: RBAC, principle of least privilege

## Perfiles de Atacante Simulados

### Perfil 1: Script Kiddie (Reconocimiento + Escaneo)
- **Motivación**: Curiosidad, reconocimiento
- **Capacidad**: Baja - usa herramientas públicas
- **TTPs**: T1595, T1595.002
- **Escenarios**: S01, S02

### Perfil 2: Cybercriminal Motivado por Dinero (Fraude Fiscal)
- **Motivación**: Robo de datos de contribuyentes, fraude al sistema tributario
- **Capacidad**: Media - técnicas de SQLi, credential stuffing
- **TTPs**: T1190, T1110.004, T1078, T1213, T1530
- **Escenarios**: S04, S05, S07

### Perfil 3: Insider Malicioso (Reverse Shell, Persistencia)
- **Motivación**: Robo de información fiscal interna
- **Capacidad**: Alta - conoce el sistema
- **TTPs**: T1059.004, T1105, T1048.003
- **Escenarios**: S08, S09, S10

### Perfil 4: State-Sponsored (Exfiltración Avanzada)
- **Motivación**: Espionaje fiscal/económico
- **Capacidad**: Muy alta - DNS tunneling, malware custom
- **TTPs**: T1048.003, T1105
- **Escenarios**: S10, S08

## Asset Inventory

### Activos Críticos (en orden de criticidad)

1. **API Tributaria** - Procesa declaraciones juradas (millones de registros)
2. **Base de datos de contribuyentes** - Información PII
3. **Portal de contribuyentes** - Interfaz de servicio al ciudadano
4. **Sistema de autenticación** - SSO, JWT tokens
5. **Sistema de facturación electrónica** - CUF codes
6. **Reportes financieros** - Datos macroeconómicos

### Activos del Laboratorio (Honeypots)

1. **Cowrie SSH/Telnet** - Atrae atacantes genéricos
2. **Dionaea SMB/FTP** - Captura malware
3. **OpenCanary HTTP/MySQL/SMB** - Detecta escaneos
4. **Heralding** - Captura credenciales
5. **Decoy API custom** - Simula API tributaria real (atractivo alto)
6. **Decoy Portal custom** - Simula portal de contribuyentes

## Attack Surface

### Expuesto a Internet (simulado en lab)
- Portal Tributario (puerto 8000)
- API Tributaria (puerto 8000)
- Cowrie SSH (puerto 2222)
- Dionaea SMB/FTP (puertos 445, 21)
- OpenCanary HTTP/SSH (puertos 80, 22)

### Solo Interno (en lab)
- Wazuh Dashboard
- TheHive + Cortex
- MISP
- Shuffle
- Velociraptor
- Grafana

## Casos de Uso de Amenazas

### Caso 1: Robo Masivo de Datos de Contribuyentes
- **Motivación**: Venta de datos PII en dark web
- **Path**: S02 (reconocimiento) → S04 (SQLi) → S07 (IDOR enumeration) → S10 (exfiltración)
- **Tiempo total**: ~2 horas
- **Impacto**: Millones de registros PII comprometidos

### Caso 2: Defacement del Portal
- **Motivación**: Hacktivismo político contra el ente tributario
- **Path**: S01 (recon) → S06 (XSS stored) → defacement
- **Tiempo total**: ~30 minutos
- **Impacto**: Imagen institucional dañada

### Caso 3: Ransomware Fiscal
- **Motivación**: Criptomoneda, desestabilización
- **Path**: S03 (brute force RDP) → S09 (reverse shell) → persistencia → cifrado
- **Tiempo total**: ~1 día
- **Impacto**: Sistemas tributarios paralizados durante semanas

### Caso 4: Fraude al Sistema Tributario
- **Motivación**: Evasión fiscal de un grupo organizado
- **Path**: S05 (credential stuffing admin) → S07 (modificación declaraciones)
- **Tiempo total**: ~3 días
- **Impacto**: Pérdida de millones en recaudación

## Conclusiones del Threat Model

1. **Vector de ataque más probable**: SQL Injection + Credential Stuffing
2. **Activo más atractivo**: API Tributaria (datos fiscales)
3. **Cadena de ataque típica**: Reconocimiento → Explotación → Exfiltración
4. **Tiempo medio de detección esperado**: <5 minutos
5. **Tiempo medio de contención esperado**: <30 minutos
