# rescate

Reto de Algoritmos: Rescate de Datos Críticos en una Infraestructura Comprometida

## 📋 Descripción del Proyecto

Este repositorio contiene el enunciado y solución completa de un proyecto de gestión de crisis que simula una situación de emergencia tecnológica. Los estudiantes deben aplicar habilidades analíticas para diseñar una solución eficiente de recuperación de datos durante un ataque de ransomware.

## 🎯 Escenario

Imagina que eres el responsable de sistemas en una empresa que gestiona datos médicos sensibles. A las 8:00 de la mañana, se detecta un ataque de ransomware que ha comprometido parcialmente la infraestructura. El equipo de seguridad ha logrado aislar el ataque, pero solo tienes **120 minutos** para rescatar los datos más críticos antes de que el sistema se reinicie automáticamente.

## 📊 Tareas del Proyecto

| Tarea | Descripción | Duración | Restricciones |
|-------|-------------|----------|---------------|
| A | Identificar servidores afectados | 15 min | - |
| B | Priorizar datos críticos | 20 min | - |
| C | Activar protocolo de recuperación | 10 min | Después de A |
| D | Asignar técnicos a servidores | 5 min | Después de B y C |
| E | Recuperar datos de servidor 1 | 30 min | Después de D |
| F | Recuperar datos de servidor 2 | 25 min | Después de E |
| G | Validar integridad de datos | 15 min | Después de E y F |
| H | Generar informe preliminar | 10 min | Después de G |
| I | Comunicar a clientes afectados | 20 min | Después de G |
| J | Coordinar con equipo legal | 15 min | Después de G |
| K | Preparar plan de contingencia | 25 min | Después de G |

### 🚫 Restricciones Críticas
- Solo hay **3 técnicos** disponibles
- Solo se pueden recuperar datos de **un servidor a la vez**
- Las tareas H, I, J y K deben comenzar **después** de validar los datos (tarea G)
- **Tiempo límite absoluto**: 120 minutos

## 🎯 Objetivos del Reto

1. **Definir el Objetivo del Proyecto**: ¿Qué se debe lograr exactamente en estos 120 minutos?
2. **Diagrama de Flujo del Cronograma**: Representa las tareas y sus dependencias
3. **Nivelación de Recursos**: Optimiza el uso de personal técnico y herramientas disponibles
4. **Plan de Comunicación de Crisis**: ¿Cómo se informa a los stakeholders internos y externos?

## 📁 Estructura del Repositorio

```
rescate/
├── README.md                          # Este archivo
├── solution/                          # Solución completa del proyecto
│   ├── project_objectives.md          # Definición de objetivos
│   ├── critical_path_analysis.md      # Análisis de ruta crítica
│   ├── resource_leveling.md           # Plan de nivelación de recursos
│   ├── crisis_communication_plan.md   # Plan de comunicación
│   ├── flowchart_diagram.md           # Diagramas de flujo
│   └── complete_solution.md           # Solución integrada
├── templates/                         # Plantillas para estudiantes
│   └── student_template.md            # Plantilla de trabajo
└── evaluation/                       # Materiales de evaluación
    └── rubric.md                     # Rúbrica detallada
```

## 🚀 Cómo Usar Este Repositorio

### Para Estudiantes
1. **Lee el enunciado completo** en este README
2. **Utiliza la plantilla** en `templates/student_template.md` para estructurar tu solución
3. **Consulta la solución** en la carpeta `solution/` solo después de intentar resolver el problema
4. **Revisa la rúbrica** en `evaluation/rubric.md` antes de entregar

### Para Profesores
1. **Asigna el proyecto** usando este README como enunciado
2. **Utiliza la rúbrica** en `evaluation/rubric.md` para evaluación
3. **Consulta la solución modelo** en `solution/` para corrección
4. **Adapta los tiempos** según el nivel de los estudiantes

## ✅ Criterios de Entrega

- **Fecha límite**: lunes 15 de septiembre de 2025, 23:55 hrs
- **Formato**: PDF
- **Nombre del archivo**: `C1_Nombre_Apellido.pdf`

## 📊 Rúbrica de Evaluación

| Categoría | Descripción | Ponderación |
|-----------|-------------|-------------|
| **Definición de Objetivos** | Claridad y enfoque en el propósito del proyecto | 20% |
| **Diagrama de Flujo del Cronograma** | Precisión en dependencias y lógica del flujo | 25% |
| **Nivelación de Recursos** | Optimización del uso de técnicos y tiempos | 20% |
| **Comunicación del Proyecto** | Claridad y eficacia con stakeholders | 20% |
| **Presentación y Formato** | Organización y cumplimiento de instrucciones | 15% |

## 🎯 Resultados Esperados

Al completar este proyecto, los estudiantes habrán demostrado:
- Habilidades de **análisis de sistemas** bajo presión
- Capacidad de **optimización de recursos** limitados
- **Gestión de proyectos** con restricciones temporales
- **Comunicación efectiva** en situaciones de crisis
- **Pensamiento crítico** para resolución de problemas complejos

## 🔧 Solución Modelo

La solución modelo incluye:
- ✅ **Tiempo total**: 120 minutos exactos
- ✅ **Utilización de recursos**: 69% de eficiencia
- ✅ **Ruta crítica**: A → C → D → E → F → G (100 minutos)
- ✅ **Margen de seguridad**: 20 minutos para tareas finales
- ✅ **Cumplimiento**: Todas las restricciones respetadas

## 📚 Recursos Adicionales

- [Templates para estudiantes](templates/)
- [Solución completa](solution/)
- [Rúbrica de evaluación](evaluation/)
- [Diagramas de flujo](solution/flowchart_diagram.md)

## 💡 Tips para Estudiantes

1. **Identifica la ruta crítica** primero
2. **Optimiza el uso de técnicos** desde el inicio
3. **Considera las restricciones** en todo momento
4. **Planifica la comunicación** como parte integral
5. **Valida tu solución** contra las restricciones de tiempo

## 🤝 Contribuciones

Este proyecto es parte del curso de Algoritmos. Para sugerencias o mejoras, contacta al profesor responsable.

---

**¡Éxito en tu proyecto de rescate de datos críticos!** 🚀

