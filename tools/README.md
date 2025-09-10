# Herramientas de Apoyo para Estudiantes

## 📊 Calculadora de Ruta Crítica

### Descripción
Script en Python que calcula automáticamente la ruta crítica del proyecto de rescate de datos, permitiendo a los estudiantes validar su análisis.

### Uso
```bash
python3 tools/critical_path_calculator.py
```

### Qué hace la herramienta:
- ✅ Calcula tiempos tempranos (ES/EF) para todas las tareas
- ✅ Calcula tiempos tardíos (LS/LF) para todas las tareas  
- ✅ Identifica la ruta crítica automáticamente
- ✅ Calcula holguras de cada tarea
- ✅ Verifica restricciones del proyecto
- ✅ Identifica problemas de tiempo (exceso de 120 min)

### Resultados esperados:
- **Ruta crítica**: A → C → D → E → F → G → K
- **Duración básica**: 125 minutos (excede límite)
- **Problema identificado**: Tarea K causa exceso de 5 minutos
- **Solución requerida**: Optimización de recursos y paralelización

## 📋 Plantilla de Trabajo

### Ubicación
`templates/student_template.md`

### Características:
- Estructura completa para la solución
- Espacios para completar cada sección
- Instrucciones paso a paso
- Checklist de entrega
- Formato apropiado para convertir a PDF

### Secciones incluidas:
1. **Definición de objetivos del proyecto**
2. **Análisis de tareas y dependencias**
3. **Diagrama de flujo del cronograma**
4. **Nivelación de recursos**
5. **Plan de comunicación de crisis**
6. **Análisis de riesgos y contingencias**
7. **Reflexión y conclusiones**

## 📚 Solución de Referencia

### Ubicación
Carpeta `solution/` con documentos detallados:

- `project_objectives.md` - Definición completa de objetivos
- `critical_path_analysis.md` - Análisis detallado de ruta crítica
- `resource_leveling.md` - Plan de optimización de recursos
- `crisis_communication_plan.md` - Estrategia de comunicación
- `flowchart_diagram.md` - Diagramas visuales y cronogramas
- `complete_solution.md` - Integración de toda la solución

### Puntos clave de la solución:
- **Tiempo total optimizado**: 120 minutos exactos
- **Utilización de recursos**: 69% de eficiencia promedio
- **Paralelización crítica**: A+B simultáneamente (ahorra 15 min)
- **Distribución final**: H,I,J,K en paralelo con 3 técnicos

## 🎯 Cómo Usar Estas Herramientas

### Para Estudiantes:

#### Paso 1: Intento inicial
1. Lee el enunciado en `README.md`
2. Intenta resolver el problema por tu cuenta
3. Usa la plantilla `templates/student_template.md`

#### Paso 2: Validación
1. Ejecuta `python3 tools/critical_path_calculator.py`
2. Compara tus resultados con la salida de la herramienta
3. Identifica discrepancias en tu análisis

#### Paso 3: Optimización
1. Si tu solución excede 120 minutos, revisa:
   - ¿Paralelizaste A y B?
   - ¿Distribuiste H,I,J,K entre 3 técnicos?
   - ¿Respetaste todas las restricciones?

#### Paso 4: Consulta de referencia
1. Solo después de intentar resolver, consulta `solution/`
2. Compara tu enfoque con la solución modelo
3. Identifica áreas de mejora

### Para Profesores:

#### Evaluación automatizada:
1. Usa `tools/critical_path_calculator.py` para verificar cálculos
2. Consulta `evaluation/rubric.md` para criterios detallados
3. Compara soluciones estudiantiles con `solution/`

#### Personalización:
- Modifica duraciones en el script para crear variantes
- Ajusta restricciones para diferentes niveles
- Usa la plantilla como base para otros proyectos

## ⚠️ Limitaciones y Consideraciones

### Lo que la herramienta NO hace:
- No optimiza automáticamente los recursos
- No genera los diagramas visuales
- No evalúa la calidad de la comunicación
- No considera aspectos de implementación práctica

### Lo que los estudiantes DEBEN hacer manualmente:
- Análisis de optimización de recursos
- Diseño de diagramas de flujo
- Desarrollo del plan de comunicación
- Evaluación crítica de la solución

## 🔧 Requisitos Técnicos

### Para usar las herramientas:
- Python 3.x (para la calculadora)
- Editor de texto (para la plantilla)
- Conversor a PDF (para la entrega final)

### Sin requisitos adicionales:
- No necesita bibliotecas externas de Python
- Funciona en cualquier sistema operativo
- Compatible con entornos de desarrollo estándar

## 📈 Resultados de Aprendizaje

Al usar estas herramientas, los estudiantes desarrollarán:

### Habilidades técnicas:
- Cálculo de ruta crítica (CPM)
- Análisis de recursos y optimización
- Gestión de restricciones temporales
- Uso de herramientas de validación

### Habilidades blandas:
- Pensamiento crítico bajo presión
- Comunicación efectiva en crisis
- Trabajo en equipo coordinado
- Toma de decisiones con información limitada

### Competencias profesionales:
- Gestión de proyectos con metodologías establecidas
- Respuesta a incidentes de seguridad
- Coordinación multi-stakeholder
- Documentación profesional de procesos

## 🚀 Extensiones Posibles

### Para estudiantes avanzados:
- Análisis de sensibilidad de tiempos
- Optimización con recursos variables
- Simulación Monte Carlo para riesgos
- Desarrollo de interfaces gráficas

### Para cursos avanzados:
- Integración con software de gestión de proyectos
- Análisis de costos además de tiempo
- Consideración de incertidumbre en duraciones
- Optimización multi-objetivo

---

**¿Necesitas ayuda adicional?**
Consulta la documentación completa en cada carpeta o contacta al instructor del curso.