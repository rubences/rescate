# Fase 1 - Preparación del Dataset Visual (CIFAR-10)

Este documento describe la implementación de la Fase 1 del proyecto, que consiste en la preparación del dataset CIFAR-10 para su uso en modelos de redes neuronales convolucionales (CNN).

## Descripción General

El script `cifar10_preparation.py` implementa todas las tareas necesarias para cargar, visualizar y preprocesar el dataset CIFAR-10, siguiendo las mejores prácticas para el entrenamiento de modelos de deep learning.

## Issues Implementadas

### ✅ Issue 1: Cargar el dataset CIFAR-10 desde tensorflow.keras.datasets

**Descripción:** Importar el dataset CIFAR-10 utilizando las utilidades disponibles en TensorFlow. Separar los datos en conjuntos de entrenamiento y prueba.

**Implementación:**
- Importa `tensorflow.keras.datasets.cifar10`
- Carga CIFAR-10 y asigna a `x_train`, `y_train`, `x_test`, `y_test`
- Verifica las dimensiones de los datos cargados
- Incluye fallback a datos de ejemplo si no hay conexión a internet

**Criterios de aceptación cumplidos:**
- ✓ El dataset se carga correctamente sin errores
- ✓ Se imprimen las formas de `x_train`, `x_test`, `y_train`, `y_test`

### ✅ Issue 2: Visualizar imágenes de cada una de las 10 categorías

**Descripción:** Mostrar al menos una imagen representativa por clase del dataset para familiarizarse con su variedad.

**Implementación:**
- Crea un mapeo entre las etiquetas (0-9) y sus nombres (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck)
- Selecciona una imagen por clase
- Usa matplotlib para mostrar las imágenes con su etiqueta correspondiente
- Guarda la visualización en `cifar10_categories.png`

**Criterios de aceptación cumplidos:**
- ✓ Se visualizan 10 imágenes, una por categoría
- ✓ Las etiquetas se muestran correctamente en el título de cada imagen

### ✅ Issue 3: Normalizar los valores de los píxeles

**Descripción:** Escalar los valores de los píxeles de las imágenes al rango [0, 1], lo cual es esencial para entrenar redes neuronales.

**Implementación:**
- Convierte `x_train` y `x_test` a tipo `float32`
- Divide por 255.0 para normalizar al rango [0, 1]

**Criterios de aceptación cumplidos:**
- ✓ Todos los valores en `x_train` y `x_test` están en el rango [0.0, 1.0]
- ✓ Se comprueba visualmente con `print(np.min(x_train), np.max(x_train))`

### ✅ Issue 4: Aplicar One-Hot Encoding a las etiquetas

**Descripción:** Convertir las etiquetas numéricas (0-9) en vectores one-hot para ser compatibles con modelos de clasificación multiclase.

**Implementación:**
- Usa `tensorflow.keras.utils.to_categorical` para convertir `y_train` y `y_test`

**Criterios de aceptación cumplidos:**
- ✓ `y_train` y `y_test` pasan de tener forma `(n,)` a `(n, 10)`
- ✓ Se verifica visualmente con `print(y_train[0])`

### ✅ Issue 5: Verificar que las imágenes no sean aplanadas

**Descripción:** Confirmar que las imágenes mantienen su estructura 2D (32x32x3) necesaria para modelos CNN.

**Implementación:**
- Comprueba las dimensiones de `x_train` y `x_test`
- Documenta que no se aplana la imagen, a diferencia del preprocesamiento para un MLP

**Criterios de aceptación cumplidos:**
- ✓ `x_train.shape[1:]` es `(32, 32, 3)`
- ✓ No se aplica `reshape` ni `flatten` a las imágenes

## Uso

### Requisitos

```bash
pip install tensorflow matplotlib numpy
```

### Ejecución

```bash
python cifar10_preparation.py
```

### Salida Esperada

El script imprimirá:
1. Información sobre la carga del dataset
2. Lista de categorías (0-9 con sus nombres)
3. Confirmación de visualización guardada
4. Rangos de valores normalizados
5. Forma de las etiquetas antes y después del one-hot encoding
6. Verificación de las dimensiones de las imágenes
7. Resumen final con todas las estadísticas

Adicionalmente, generará el archivo `cifar10_categories.png` con las visualizaciones.

## Estructura del Dataset

### Dataset Original
- **Imágenes de entrenamiento:** `(50000, 32, 32, 3)` - 50,000 imágenes RGB de 32x32 píxeles
- **Imágenes de prueba:** `(10000, 32, 32, 3)` - 10,000 imágenes RGB de 32x32 píxeles
- **Etiquetas de entrenamiento:** `(50000, 1)` - Valores de 0-9
- **Etiquetas de prueba:** `(10000, 1)` - Valores de 0-9

### Dataset Procesado
- **Imágenes de entrenamiento:** `(50000, 32, 32, 3)` - Normalizadas al rango [0, 1]
- **Imágenes de prueba:** `(10000, 32, 32, 3)` - Normalizadas al rango [0, 1]
- **Etiquetas de entrenamiento:** `(50000, 10)` - One-hot encoded
- **Etiquetas de prueba:** `(10000, 10)` - One-hot encoded

## Categorías CIFAR-10

| Índice | Categoría |
|--------|-----------|
| 0 | airplane (avión) |
| 1 | automobile (automóvil) |
| 2 | bird (pájaro) |
| 3 | cat (gato) |
| 4 | deer (ciervo) |
| 5 | dog (perro) |
| 6 | frog (rana) |
| 7 | horse (caballo) |
| 8 | ship (barco) |
| 9 | truck (camión) |

## Notas Importantes

1. **Normalización:** La normalización de los píxeles es crucial para el entrenamiento efectivo de redes neuronales, ya que ayuda a la convergencia del modelo.

2. **One-Hot Encoding:** La codificación one-hot convierte las etiquetas numéricas en vectores binarios, lo cual es necesario para la función de pérdida categorical_crossentropy.

3. **Estructura 2D:** A diferencia de los MLP (Multi-Layer Perceptron), las CNN requieren que las imágenes mantengan su estructura espacial 2D, por lo que NO se aplanan.

4. **Modo Mock:** El script incluye un modo de datos de ejemplo que se activa automáticamente si no puede descargar el dataset real (útil para desarrollo sin conexión a internet).

## Próximos Pasos

Después de completar la preparación del dataset, los siguientes pasos típicos incluirían:

1. Diseño de la arquitectura de la CNN
2. Compilación del modelo con optimizador y función de pérdida apropiados
3. Entrenamiento del modelo
4. Evaluación del rendimiento
5. Ajuste de hiperparámetros

## Referencias

- [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)
- [TensorFlow/Keras Documentation](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10)
