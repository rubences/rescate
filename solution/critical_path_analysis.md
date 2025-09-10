# Análisis de Dependencias y Ruta Crítica

## Definición de Tareas y Dependencias

### Lista de Tareas
| Tarea | Descripción | Duración | Predecesoras | Recursos |
|-------|-------------|----------|--------------|----------|
| A | Identificar servidores afectados | 15 min | - | 1 técnico |
| B | Priorizar datos críticos | 20 min | - | 1 técnico |
| C | Activar protocolo de recuperación | 10 min | A | 1 técnico |
| D | Asignar técnicos a servidores | 5 min | B, C | 1 técnico |
| E | Recuperar datos de servidor 1 | 30 min | D | 1 técnico |
| F | Recuperar datos de servidor 2 | 25 min | E | 1 técnico |
| G | Validar integridad de datos | 15 min | E, F | 1 técnico |
| H | Generar informe preliminar | 10 min | G | 1 técnico |
| I | Comunicar a clientes afectados | 20 min | G | 1 técnico |
| J | Coordinar con equipo legal | 15 min | G | 1 técnico |
| K | Preparar plan de contingencia | 25 min | G | 1 técnico |

## Análisis de la Ruta Crítica

### Cálculo de Tiempos Tempranos (ES/EF)
```
A: ES=0, EF=15
B: ES=0, EF=20
C: ES=15, EF=25  (depende de A)
D: ES=25, EF=30  (depende de B y C, toma el máximo: max(20,25)=25)
E: ES=30, EF=60  (depende de D)
F: ES=60, EF=85  (depende de E, restricción de un servidor a la vez)
G: ES=85, EF=100 (depende de E y F)
H: ES=100, EF=110 (depende de G)
I: ES=100, EF=120 (depende de G)
J: ES=100, EF=115 (depende de G)
K: ES=100, EF=125 (depende de G) ⚠️ EXCEDE 120 MINUTOS
```

### Cálculo de Tiempos Tardíos (LS/LF)
```
Para que K termine en 120 min máximo:
K: LS=95, LF=120
G: LS=80, LF=95   (para permitir H,I,J,K)
F: LS=55, LF=80   (para permitir G)
E: LS=25, LF=55   (para permitir F)
D: LS=20, LF=25   (para permitir E)
C: LS=15, LF=25   (para permitir D)
B: LS=0, LF=20    (para permitir D)
A: LS=0, LF=15    (para permitir C)
```

### Identificación de la Ruta Crítica
**Ruta Crítica: A → C → D → E → F → G**
- Duración total de la ruta crítica: 15 + 10 + 5 + 30 + 25 + 15 = **100 minutos**

### Holguras de las Tareas
| Tarea | Holgura Total | ¿Es Crítica? |
|-------|---------------|--------------|
| A | 0 min | ✅ SÍ |
| B | 5 min | ❌ No |
| C | 0 min | ✅ SÍ |
| D | 0 min | ✅ SÍ |
| E | 0 min | ✅ SÍ |
| F | 0 min | ✅ SÍ |
| G | 0 min | ✅ SÍ |
| H | 10 min | ❌ No |
| I | 0 min | ⚠️ Crítica para límite de 120 min |
| J | 5 min | ❌ No |
| K | -5 min | 🚨 **PROBLEMA** |

## Problemas Identificados

### ⚠️ Conflicto de Tiempo
- La tarea K (Preparar plan de contingencia) requiere 25 minutos
- Solo quedan 20 minutos después de completar G (minuto 100 al 120)
- **Déficit: 5 minutos**

## Soluciones Propuestas

### Opción 1: Paralelización de Tareas Finales
- Ejecutar H, I, J simultáneamente después de G (requiere 3 técnicos)
- Iniciar K en paralelo, limitándola a 20 minutos

### Opción 2: Optimización de Recursos
- Ejecutar B en paralelo con A (usando 2 técnicos desde el inicio)
- Ganar 5 minutos en la fase inicial

### Opción 3: Reducción de Alcance
- Reducir el tiempo de K a 20 minutos
- Priorizar las tareas más críticas (H, I, J)

## Cronograma Optimizado Recomendado

### Fase 1 (0-25 min): Preparación Inicial
- **Minutos 0-15**: Técnico 1 ejecuta A
- **Minutos 0-20**: Técnico 2 ejecuta B 
- **Minutos 15-25**: Técnico 1 ejecuta C

### Fase 2 (25-85 min): Recuperación de Datos
- **Minutos 25-30**: Técnico 1 ejecuta D
- **Minutos 30-60**: Técnico 1 ejecuta E
- **Minutos 60-85**: Técnico 1 ejecuta F

### Fase 3 (85-100 min): Validación
- **Minutos 85-100**: Técnico 1 ejecuta G

### Fase 4 (100-120 min): Comunicación y Documentación
- **Minutos 100-110**: Técnico 1 ejecuta H
- **Minutos 100-120**: Técnico 2 ejecuta I
- **Minutos 100-115**: Técnico 3 ejecuta J
- **Minutos 100-120**: Reducir K a 20 minutos (ejecutar en paralelo)

## Tiempo Total: 120 minutos exactos ✅