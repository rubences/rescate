# Plan de Comunicación de Crisis

## Principios de Comunicación en Crisis

### Principios Fundamentales
1. **Transparencia controlada**: Información veraz sin crear pánico
2. **Oportunidad**: Comunicar en el momento adecuado
3. **Consistencia**: Mensajes alineados entre todos los canales
4. **Responsabilidad**: Asumir el liderazgo en la comunicación
5. **Empatía**: Reconocer el impacto en stakeholders

## Stakeholders y Audiencias Objetivo

### Stakeholders Internos

#### 1. Alta Dirección / Junta Directiva
- **Prioridad**: Máxima
- **Información requerida**: Estado general, impacto financiero, timeline de resolución
- **Frecuencia**: Updates cada 30 minutos
- **Canal**: Llamada directa + informe escrito

#### 2. Equipo de Sistemas y TI
- **Prioridad**: Máxima
- **Información requerida**: Detalles técnicos, progreso de recuperación
- **Frecuencia**: Updates cada 15 minutos
- **Canal**: Chat interno + reuniones técnicas

#### 3. Departamento Legal
- **Prioridad**: Alta
- **Información requerida**: Datos afectados, implications regulatorias
- **Frecuencia**: Update inmediato + seguimiento cada 45 minutos
- **Canal**: Reunión presencial/virtual + documentación formal

#### 4. Recursos Humanos
- **Prioridad**: Media
- **Información requerida**: Impacto en empleados, medidas de contingencia
- **Frecuencia**: Update inicial + update final
- **Canal**: Email + reunión informativa

### Stakeholders Externos

#### 1. Clientes Afectados
- **Prioridad**: Máxima
- **Información requerida**: Qué datos fueron afectados, medidas tomadas, siguiente pasos
- **Timing**: Después de validar integridad de datos (post minuto 100)
- **Canal**: Email personalizado + llamadas a clientes críticos

#### 2. Autoridades Regulatorias
- **Prioridad**: Alta
- **Información requerida**: Notificación del incidente, datos comprometidos
- **Timing**: Dentro de las primeras 24 horas
- **Canal**: Notificación formal + seguimiento telefónico

#### 3. Medios de Comunicación
- **Prioridad**: Media (solo si es necesario)
- **Información requerida**: Declaración oficial controlada
- **Timing**: Solo si hay exposición pública
- **Canal**: Comunicado de prensa oficial

## Cronograma de Comunicación

### Fase 1: Comunicación Inmediata (0-30 min)

#### Minuto 0-5: Activación del Plan
```
Responsable: Director de TI
Acciones:
- Notificar a CEO/CTO del incidente
- Activar equipo de crisis
- Enviar alerta inicial al equipo técnico
```

#### Minuto 5-15: Evaluación Inicial
```
Responsable: Líder del Proyecto de Recuperación
Acciones:
- Informar estimación inicial a dirección
- Activar protocolo de comunicación de crisis
- Preparar primera actualización
```

#### Minuto 15-30: Primera Actualización
```
Responsable: Director de TI + CEO
Audiencia: Alta dirección, equipo legal, gerentes clave
Mensaje: "Incidente detectado, equipo activado, evaluando alcance"
```

### Fase 2: Comunicación Durante Recuperación (30-100 min)

#### Minuto 30: Update Técnico
```
Responsable: Líder Técnico
Audiencia: Equipo de TI, dirección
Mensaje: "Iniciando recuperación de datos, timeline confirmado"
```

#### Minuto 60: Update de Progreso
```
Responsable: Líder Técnico
Audiencia: Todos los stakeholders internos
Mensaje: "50% progreso completado, servidor 1 recuperado exitosamente"
```

#### Minuto 85: Update Pre-Validación
```
Responsable: Líder Técnico
Audiencia: Dirección, equipo legal
Mensaje: "Datos recuperados, iniciando validación de integridad"
```

### Fase 3: Comunicación Post-Validación (100-120 min)

#### Minuto 100: Activación Comunicación Externa
```
Responsable: Director de Comunicaciones + Legal
Preparar: Mensajes para clientes y autoridades
Validar: Contenido legal y técnico
```

#### Minuto 105: Comunicación a Clientes
```
Responsable: Especialista en Datos (T2)
Audiencia: Clientes afectados
Canal: Email + llamadas prioritarias
```

#### Minuto 115: Comunicación Oficial
```
Responsable: CEO
Audiencia: Todos los stakeholders
Mensaje: "Incidente resuelto, datos recuperados, medidas implementadas"
```

## Plantillas de Mensajes

### Template 1: Notificación Inicial a Dirección
```
ASUNTO: ALERTA CRÍTICA - Incidente de Seguridad Detectado

Estimado/a [NOMBRE],

A las [HORA] se detectó un incidente de seguridad que afecta parcialmente 
nuestra infraestructura de datos médicos.

ESTADO ACTUAL:
- Equipo de respuesta activado
- Sistemas críticos aislados
- Iniciando protocolo de recuperación

PRÓXIMOS PASOS:
- Evaluación completa en 15 minutos
- Timeline de recuperación en 30 minutos
- Updates cada 30 minutos

Contacto: [LÍDER TÉCNICO] - [TELÉFONO]

[FIRMA]
Director de TI
```

### Template 2: Comunicación a Clientes
```
ASUNTO: Notificación Importante sobre la Seguridad de sus Datos

Estimado/a [NOMBRE CLIENTE],

Le escribimos para informarle sobre un incidente de seguridad que afectó 
temporalmente nuestros sistemas el día [FECHA].

QUÉ OCURRIÓ:
- Detectamos actividad no autorizada en nuestros servidores
- El incidente fue aislado inmediatamente
- Los datos fueron recuperados exitosamente

SUS DATOS:
- Hemos verificado la integridad de su información
- No hay evidencia de acceso no autorizado a datos sensibles
- Todos los sistemas están operando normalmente

MEDIDAS TOMADAS:
- Protocolos de seguridad reforzados
- Auditoría completa del sistema
- Plan de contingencia actualizado

Para cualquier pregunta, contacte: [CONTACTO]

Atentamente,
[NOMBRE]
Director General
```

### Template 3: Comunicado Interno Post-Resolución
```
ASUNTO: Resolución Exitosa del Incidente de Seguridad

Equipo,

Nos complace informar que el incidente de seguridad ha sido resuelto 
exitosamente.

RESUMEN:
- Duración: 120 minutos
- Datos recuperados: 100%
- Sistemas operativos: Completamente funcionales
- Clientes notificados: Todos

PRÓXIMOS PASOS:
- Análisis post-incidente esta semana
- Actualización de protocolos
- Capacitación adicional del equipo

Gracias por su profesionalismo durante esta situación.

[FIRMA]
```

## Gestión de Canales de Comunicación

### Canales Internos

#### 1. Sistema de Alertas Críticas
- **Herramienta**: SMS + Email + Slack
- **Audiencia**: Equipo de crisis
- **Uso**: Notificaciones inmediatas

#### 2. Dashboard de Crisis
- **Herramienta**: Pantalla compartida en tiempo real
- **Audiencia**: Todos los stakeholders internos
- **Uso**: Status updates visuales

#### 3. Videoconferencia de Crisis
- **Herramienta**: Zoom/Teams
- **Audiencia**: Liderazgo ejecutivo
- **Uso**: Updates cada 30 minutos

### Canales Externos

#### 1. Portal de Clientes
- **Herramienta**: Website + App
- **Audiencia**: Todos los clientes
- **Uso**: Updates generales

#### 2. Email Directo
- **Herramienta**: Sistema CRM
- **Audiencia**: Clientes prioritarios
- **Uso**: Comunicación personalizada

#### 3. Línea de Atención
- **Herramienta**: Call center
- **Audiencia**: Clientes con consultas
- **Uso**: Soporte durante y post-crisis

## Métricas y Monitoreo

### KPIs de Comunicación
1. **Tiempo de primera notificación**: < 5 minutos
2. **Cobertura de stakeholders**: 100%
3. **Precisión de información**: Sin contradicciones
4. **Tiempo de respuesta a consultas**: < 2 horas

### Monitoreo de Reputación
- **Redes sociales**: Monitoreo de menciones
- **Medios tradicionales**: Seguimiento de noticias
- **Feedback de clientes**: Análisis de respuestas

## Plan de Contingencia de Comunicación

### Escenarios de Falla
1. **Extensión del tiempo de recuperación**: Mensajes de actualización
2. **Pérdida parcial de datos**: Comunicación de crisis ampliada
3. **Exposición mediática**: Activación del protocolo de medios

### Recursos de Respaldo
- **Portavoz alternativo**: Director de Operaciones
- **Canales secundarios**: Redes sociales corporativas
- **Soporte externo**: Agencia de comunicaciones de crisis