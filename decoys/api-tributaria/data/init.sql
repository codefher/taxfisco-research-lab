-- =============================================================================
-- Datos fiscales de ejemplo. Contribuyentes, NIT y CUF ficticios.
-- Ningun registro corresponde a un contribuyente real.
-- =============================================================================
-- Datos sintéticos NO REALES - Solo para honeypot research
-- =============================================================================

CREATE TABLE IF NOT EXISTS contribuyentes (
    id SERIAL PRIMARY KEY,
    nit VARCHAR(20) UNIQUE NOT NULL,
    razon_social VARCHAR(255) NOT NULL,
    tipo_persona VARCHAR(20) NOT NULL CHECK (tipo_persona IN ('NATURAL', 'JURIDICA')),
    estado VARCHAR(20) DEFAULT 'ACTIVO' CHECK (estado IN ('ACTIVO', 'INACTIVO', 'SUSPENDIDO')),
    fecha_inscripcion DATE DEFAULT CURRENT_DATE,
    domicilio_fiscal JSONB,
    contacto JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS declaraciones_juradas (
    id SERIAL PRIMARY KEY,
    id_declaracion VARCHAR(50) UNIQUE NOT NULL,
    nit_contribuyente VARCHAR(20) REFERENCES contribuyentes(nit),
    periodo VARCHAR(7) NOT NULL,
    tipo_declaracion VARCHAR(20) NOT NULL CHECK (tipo_declaracion IN ('IVA', 'IT', 'IUE', 'RC-IVA')),
    monto_declarado DECIMAL(15, 2) NOT NULL,
    monto_pagado DECIMAL(15, 2),
    estado VARCHAR(20) DEFAULT 'RECIBIDA',
    fecha_recepcion TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS facturas (
    id SERIAL PRIMARY KEY,
    cuf VARCHAR(55) UNIQUE NOT NULL,
    nit_emisor VARCHAR(20) REFERENCES contribuyentes(nit),
    nit_receptor VARCHAR(20) REFERENCES contribuyentes(nit),
    monto DECIMAL(15, 2) NOT NULL,
    fecha_emision DATE NOT NULL,
    estado VARCHAR(20) DEFAULT 'VALIDA'
);

CREATE TABLE IF NOT EXISTS sesiones_activas (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(128) UNIQUE NOT NULL,
    user_id INTEGER,
    ip_origen VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    last_activity TIMESTAMP DEFAULT NOW(),
    is_deception BOOLEAN DEFAULT FALSE
);

-- Insertar contribuyentes sintéticos
INSERT INTO contribuyentes (nit, razon_social, tipo_persona, estado, domicilio_fiscal) VALUES
    ('10234567891', 'CONSTRUCTORA ANDINA S.A.', 'JURIDICA', 'ACTIVO', '{"departamento": "La Paz", "zona": "Zona 1"}'),
    ('10987654321', 'SERVICIOS FINANCIEROS DEL SUR S.A.', 'JURIDICA', 'ACTIVO', '{"departamento": "Santa Cruz", "zona": "Zona 2"}'),
    ('11456789012', 'DISTRIBUIDORA LOPEZ S.R.L.', 'JURIDICA', 'ACTIVO', '{"departamento": "Cochabamba", "zona": "Zona 3"}'),
    ('12345678901', 'IMPORTADORA BOLIVIANA S.A.', 'JURIDICA', 'ACTIVO', '{"departamento": "La Paz", "zona": "Zona 1"}'),
    ('13141516171', 'CONSULTORIA ESTRATEGICA GLOBAL S.R.L.', 'JURIDICA', 'ACTIVO', '{"departamento": "Santa Cruz", "zona": "Zona 2"}'),
    ('18192021222', 'INDUSTRIAS MANUFACTURERAS DEL NORTE S.A.', 'JURIDICA', 'ACTIVO', '{"departamento": "Cochabamba", "zona": "Zona 3"}'),
    ('10000001001', 'AGROPECUARIA SAN MIGUEL LTDA.', 'JURIDICA', 'INACTIVO', '{"departamento": "Tarija", "zona": "Zona 4"}'),
    ('10000002002', 'TRANSPORTES RAPIDOS DEL SUR S.R.L.', 'JURIDICA', 'ACTIVO', '{"departamento": "Oruro", "zona": "Zona 5"}'),
    ('10000003003', 'COMERCIALIZADORA ANDINA S.A.', 'JURIDICA', 'ACTIVO', '{"departamento": "Potosi", "zona": "Zona 6"}'),
    ('10000004004', 'FARMACIA CENTRAL LTDA.', 'JURIDICA', 'ACTIVO', '{"departamento": "Chuquisaca", "zona": "Zona 7"}')
ON CONFLICT (nit) DO NOTHING;

-- Insertar declaraciones
INSERT INTO declaraciones_juradas (id_declaracion, nit_contribuyente, periodo, tipo_declaracion, monto_declarado, monto_pagado, estado) VALUES
    ('DJ-2024-11-000001', '10234567891', '2024-11', 'IVA', 125000.50, 125000.50, 'PROCESADA'),
    ('DJ-2024-11-000002', '10987654321', '2024-11', 'IT', 87500.00, 87500.00, 'PROCESADA'),
    ('DJ-2024-11-000003', '11456789012', '2024-11', 'IUE', 234000.00, 234000.00, 'PROCESADA'),
    ('DJ-2024-12-000001', '10234567891', '2024-12', 'IVA', 132500.75, 0.00, 'PENDIENTE'),
    ('DJ-2024-12-000002', '12345678901', '2024-12', 'IT', 95200.00, 0.00, 'PENDIENTE')
ON CONFLICT (id_declaracion) DO NOTHING;

-- Insertar facturas
INSERT INTO facturas (cuf, nit_emisor, nit_receptor, monto, fecha_emision) VALUES
    ('1234567890123456789012345678901234567890123456789012340', '10234567891', '10987654321', 4500.00, '2024-12-01'),
    ('2234567890123456789012345678901234567890123456789012340', '10987654321', '11456789012', 12300.50, '2024-12-05'),
    ('3234567890123456789012345678901234567890123456789012340', '11456789012', '12345678901', 8900.00, '2024-12-10'),
    ('4234567890123456789012345678901234567890123456789012340', '10234567891', '13141516171', 56000.00, '2024-12-12'),
    ('5234567890123456789012345678901234567890123456789012340', '12345678901', '18192021222', 3400.00, '2024-12-14')
ON CONFLICT (cuf) DO NOTHING;

-- Crear índices
CREATE INDEX idx_contribuyentes_nit ON contribuyentes(nit);
CREATE INDEX idx_declaraciones_periodo ON declaraciones_juradas(periodo);
CREATE INDEX idx_facturas_fecha ON facturas(fecha_emision);
CREATE INDEX idx_sesiones_session ON sesiones_activas(session_id);
