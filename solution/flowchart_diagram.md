# Diagrama de Flujo del Cronograma

## Representación Visual del Flujo de Tareas

```
                        INICIO DEL INCIDENTE (t=0)
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
            ┌───────▼─────────┐           ┌────────▼────────┐
            │   A: Identificar │           │  B: Priorizar   │
            │   servidores     │           │  datos críticos │
            │   (15 min)       │           │   (20 min)      │
            │   [T1]           │           │   [T2]          │
            └───────┬─────────┘           └────────┬────────┘
                    │                               │
            ┌───────▼─────────┐                     │
            │  C: Activar     │                     │
            │  protocolo      │                     │
            │  (10 min)       │                     │
            │  [T1]           │                     │
            └───────┬─────────┘                     │
                    │              ┌────────────────┘
                    │              │
                    ▼              ▼
            ┌─────────────────────────────────┐
            │     D: Asignar técnicos         │
            │         (5 min)                 │
            │         [T1]                    │
            └─────────────┬───────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────┐
            │    E: Recuperar Servidor 1      │
            │         (30 min)                │
            │         [T1]                    │
            └─────────────┬───────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────┐
            │    F: Recuperar Servidor 2      │
            │         (25 min)                │
            │         [T1]                    │
            └─────────────┬───────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────┐
            │   G: Validar integridad         │
            │         (15 min)                │
            │         [T1]                    │
            └─────────────┬───────────────────┘
                          │
    ┌─────────────────────┼─────────────────────┐
    │                     │                     │
    │                     │                     │
    ▼                     ▼                     ▼
┌─────────┐        ┌──────────────┐     ┌─────────────┐
│H: Informe│        │ I: Comunicar │     │ J: Coordinar│
│preliminar│        │  clientes    │     │    legal    │
│(10 min) │        │  (20 min)    │     │  (15 min)   │
│  [T1]   │        │    [T2]      │     │    [T3]     │
└─────────┘        └──────────────┘     └─────────────┘
                                                │
                                                ▼
                                        ┌─────────────┐
                                        │K: Plan      │
                                        │contingencia │
                                        │ (20 min)    │
                                        │   [T3]      │
                                        └─────────────┘
                                                │
                                                ▼
                                    FIN DEL PROCESO (t=120)
```

## Diagrama de Gantt Detallado

```
Tarea │ 0    15   30   45   60   75   90   105  120
──────┼─────────────────────────────────────────────
  A   │ ████████████████
  B   │ ██████████████████████████
  C   │                ████████████
  D   │                          ████
  E   │                              ████████████████████████████████████
  F   │                                                    ████████████████████████████
  G   │                                                                      ████████████████
  H   │                                                                                  ████████
  I   │                                                                                  ████████████████████
  J   │                                                                                  ████████████████
  K   │                                                                                            ████████████████
──────┴─────────────────────────────────────────────
Técnico │
  T1   │ ████████████████████████████████████████████████████████████████████████████████████████████████████████
  T2   │ ██████████████████████████                                                              ████████████████████
  T3   │                                                                                        ████████████████████████
```

## Dependencias Críticas

### Nivel 1: Tareas Iniciales (Paralelas)
```
┌─────────────┐    ┌─────────────┐
│      A      │    │      B      │
│  (0-15 min) │    │  (0-20 min) │
└─────────────┘    └─────────────┘
```

### Nivel 2: Activación de Protocolos
```
┌─────────────┐
│      C      │ ← Depende de A
│ (15-25 min) │
└─────────────┘
```

### Nivel 3: Coordinación
```
┌─────────────┐
│      D      │ ← Depende de B y C (max)
│ (25-30 min) │
└─────────────┘
```

### Nivel 4: Recuperación Secuencial (Ruta Crítica)
```
┌─────────────┐    ┌─────────────┐
│      E      │ →  │      F      │
│ (30-60 min) │    │ (60-85 min) │
└─────────────┘    └─────────────┘
```

### Nivel 5: Validación Obligatoria
```
┌─────────────┐
│      G      │ ← Depende de E y F
│(85-100 min) │
└─────────────┘
```

### Nivel 6: Tareas Finales (Paralelas)
```
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│      H      │  │      I      │  │      J      │
│(100-110 min)│  │(100-120 min)│  │(100-115 min)│
└─────────────┘  └─────────────┘  └─────┬───────┘
                                        │
                                        ▼
                                ┌─────────────┐
                                │      K      │
                                │(110-120 min)│
                                └─────────────┘
```

## Análisis de Tipos de Dependencias

### 1. Dependencias de Finalización (Finish-to-Start)
- **A → C**: C no puede comenzar hasta que A termine
- **C → D**: D requiere protocolo activado
- **D → E**: E requiere asignación de técnicos
- **E → F**: F debe esperar que E termine (restricción de servidor)
- **F → G**: G requiere datos de ambos servidores
- **G → H,I,J,K**: Todas las tareas finales requieren validación

### 2. Dependencias de Recursos
- **T1 (Líder)**: Ejecuta ruta crítica completa
- **T2 (Especialista)**: B en paralelo, luego I
- **T3 (Analista)**: Soporte en J y K

### 3. Dependencias de Restricciones
- **Hardware**: Solo un servidor a la vez (E y F secuenciales)
- **Tiempo**: Límite absoluto de 120 minutos
- **Información**: H,I,J,K requieren datos validados

## Puntos de Decisión Críticos

### Decision Point 1 (Minuto 25)
```
     ¿A y B completadas?
            │
    ┌───────┴───────┐
    │ SÍ            │ NO
    ▼               ▼
Proceder con D    Activar
                contingencia
```

### Decision Point 2 (Minuto 85)
```
  ¿Datos recuperados exitosamente?
            │
    ┌───────┴───────┐
    │ SÍ            │ NO
    ▼               ▼
Proceder con G    Protocolo de
                  crisis extendida
```

### Decision Point 3 (Minuto 100)
```
    ¿Validación exitosa?
            │
    ┌───────┴───────┐
    │ SÍ            │ NO
    ▼               ▼
Comunicación      Comunicación
normal           de crisis
```

## Diagramas de Red (CPM)

### Cálculo del Camino Crítico
```
      15        10        5         30        25        15
  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
  │  A   │→ │  C   │→ │  D   │→ │  E   │→ │  F   │→ │  G   │
  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘  └──────┘
     0         15        25        30        60        85

      20
  ┌──────┐
  │  B   │→ [Converge en D]
  └──────┘
     0
```

**Duración total del camino crítico: 100 minutos**
**Margen disponible: 20 minutos**

## Optimizaciones Visuales

### Antes de la Optimización
```
T1: A──────C──D──E─────────F────────G──H──I────────
T2: [idle]────────────────────────────────────────
T3: [idle]────────────────────────────────────────
```

### Después de la Optimización
```
T1: A──────C──D──E─────────F────────G──H──[super]─
T2: B─────────────────────────────────────I──────
T3: [standby]─────────────────────────────J──K────
```

## Leyenda de Símbolos

- **████**: Tarea en ejecución
- **→**: Dependencia obligatoria
- **[T1/T2/T3]**: Técnico asignado
- **┌─┐**: Nodo de tarea
- **◆**: Punto de decisión crítico
- **▼**: Flujo de dependencias
- **⚠️**: Punto de control obligatorio