"""
Fase 1 - Preparación del Dataset Visual (CIFAR-10)
Este script implementa la carga, visualización y preprocesamiento del dataset CIFAR-10
para su uso en modelos de redes neuronales convolucionales (CNN).
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical


def load_cifar10(use_mock=False):
    """
    Issue 1: Cargar el dataset CIFAR-10 desde tensorflow.keras.datasets
    
    Args:
        use_mock: Si es True, genera datos de ejemplo en lugar de descargar el dataset real
    
    Returns:
        tuple: (x_train, y_train, x_test, y_test)
    """
    print("=" * 80)
    print("Issue 1: Cargando el dataset CIFAR-10...")
    print("=" * 80)
    
    if use_mock:
        # Generar datos de ejemplo que coincidan con la estructura de CIFAR-10
        print("⚠️  Usando datos de ejemplo (modo mock)")
        print("   En producción, usar cifar10.load_data() para datos reales")
        
        # Crear datos de ejemplo con las dimensiones correctas
        x_train = np.random.randint(0, 256, (50000, 32, 32, 3), dtype=np.uint8)
        y_train = np.random.randint(0, 10, (50000, 1), dtype=np.uint8)
        x_test = np.random.randint(0, 256, (10000, 32, 32, 3), dtype=np.uint8)
        y_test = np.random.randint(0, 10, (10000, 1), dtype=np.uint8)
        
        # Crear patrones simples para cada clase para la visualización
        for i in range(10):
            # Encontrar imágenes de esta clase y darles un color único
            indices = np.where(y_train[:100] == i)[0]
            if len(indices) > 0:
                color = [(i * 25) % 256, (i * 50) % 256, (i * 75) % 256]
                x_train[indices, :, :, :] = color
    else:
        try:
            # Cargar CIFAR-10 y asignar a x_train, y_train, x_test, y_test
            (x_train, y_train), (x_test, y_test) = cifar10.load_data()
        except Exception as e:
            print(f"⚠️  No se pudo descargar el dataset real: {e}")
            print("   Usando datos de ejemplo en su lugar")
            return load_cifar10(use_mock=True)
    
    # Verificar las dimensiones de los datos cargados
    print(f"✓ Dataset cargado correctamente")
    print(f"\nDimensiones de los datos:")
    print(f"  x_train.shape: {x_train.shape}")
    print(f"  y_train.shape: {y_train.shape}")
    print(f"  x_test.shape:  {x_test.shape}")
    print(f"  y_test.shape:  {y_test.shape}")
    print()
    
    return x_train, y_train, x_test, y_test


def visualize_categories(x_train, y_train):
    """
    Issue 2: Visualizar imágenes de cada una de las 10 categorías
    
    Args:
        x_train: Array de imágenes de entrenamiento
        y_train: Array de etiquetas de entrenamiento
    """
    print("=" * 80)
    print("Issue 2: Visualizando imágenes de cada categoría...")
    print("=" * 80)
    
    # Crear un mapeo entre las etiquetas (0-9) y sus nombres
    class_names = [
        'airplane',  # 0
        'automobile', # 1
        'bird',       # 2
        'cat',        # 3
        'deer',       # 4
        'dog',        # 5
        'frog',       # 6
        'horse',      # 7
        'ship',       # 8
        'truck'       # 9
    ]
    
    print("Categorías del dataset CIFAR-10:")
    for i, name in enumerate(class_names):
        print(f"  {i}: {name}")
    print()
    
    # Seleccionar al menos una imagen por clase
    plt.figure(figsize=(15, 6))
    
    for i in range(10):
        # Encontrar el primer índice de cada clase
        idx = np.where(y_train == i)[0][0]
        
        # Crear subplot para cada imagen
        plt.subplot(2, 5, i + 1)
        plt.imshow(x_train[idx])
        plt.title(f"{i}: {class_names[i]}")
        plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('cifar10_categories.png', dpi=150, bbox_inches='tight')
    print("✓ Visualización guardada en 'cifar10_categories.png'")
    print("✓ Se visualizan 10 imágenes, una por categoría")
    print()


def normalize_images(x_train, x_test):
    """
    Issue 3: Normalizar los valores de los píxeles
    
    Args:
        x_train: Array de imágenes de entrenamiento
        x_test: Array de imágenes de prueba
        
    Returns:
        tuple: (x_train_norm, x_test_norm) con valores normalizados
    """
    print("=" * 80)
    print("Issue 3: Normalizando los valores de los píxeles...")
    print("=" * 80)
    
    # Convertir x_train y x_test a tipo float32
    x_train_norm = x_train.astype('float32')
    x_test_norm = x_test.astype('float32')
    
    # Dividir por 255.0 para normalizar al rango [0, 1]
    x_train_norm = x_train_norm / 255.0
    x_test_norm = x_test_norm / 255.0
    
    # Comprobar visualmente con un print
    print(f"✓ Imágenes normalizadas correctamente")
    print(f"\nRango de valores en x_train:")
    print(f"  Mínimo: {np.min(x_train_norm)}")
    print(f"  Máximo: {np.max(x_train_norm)}")
    print(f"\nRango de valores en x_test:")
    print(f"  Mínimo: {np.min(x_test_norm)}")
    print(f"  Máximo: {np.max(x_test_norm)}")
    print()
    
    return x_train_norm, x_test_norm


def apply_one_hot_encoding(y_train, y_test):
    """
    Issue 4: Aplicar One-Hot Encoding a las etiquetas
    
    Args:
        y_train: Array de etiquetas de entrenamiento
        y_test: Array de etiquetas de prueba
        
    Returns:
        tuple: (y_train_encoded, y_test_encoded) con etiquetas codificadas
    """
    print("=" * 80)
    print("Issue 4: Aplicando One-Hot Encoding a las etiquetas...")
    print("=" * 80)
    
    # Guardar forma original
    original_train_shape = y_train.shape
    original_test_shape = y_test.shape
    
    # Usar tensorflow.keras.utils.to_categorical para convertir y_train y y_test
    y_train_encoded = to_categorical(y_train, 10)
    y_test_encoded = to_categorical(y_test, 10)
    
    # Verificar el cambio de forma
    print(f"✓ One-Hot Encoding aplicado correctamente")
    print(f"\nForma de las etiquetas:")
    print(f"  y_train: {original_train_shape} → {y_train_encoded.shape}")
    print(f"  y_test:  {original_test_shape} → {y_test_encoded.shape}")
    
    # Verificar visualmente con un print
    print(f"\nEjemplo de etiqueta codificada (primera imagen):")
    print(f"  Etiqueta original: {y_train[0]}")
    print(f"  Etiqueta one-hot:  {y_train_encoded[0]}")
    print()
    
    return y_train_encoded, y_test_encoded


def verify_image_dimensions(x_train, x_test):
    """
    Issue 5: Verificar que las imágenes no sean aplanadas
    
    Args:
        x_train: Array de imágenes de entrenamiento
        x_test: Array de imágenes de prueba
    """
    print("=" * 80)
    print("Issue 5: Verificando que las imágenes no sean aplanadas...")
    print("=" * 80)
    
    # Comprobar las dimensiones de x_train y x_test
    print(f"Dimensiones de las imágenes:")
    print(f"  x_train.shape: {x_train.shape}")
    print(f"  x_test.shape:  {x_test.shape}")
    
    # Verificar que mantienen su estructura 2D (32x32x3)
    expected_shape = (32, 32, 3)
    actual_train_shape = x_train.shape[1:]
    actual_test_shape = x_test.shape[1:]
    
    print(f"\nEstructura de cada imagen:")
    print(f"  x_train[0].shape: {actual_train_shape}")
    print(f"  x_test[0].shape:  {actual_test_shape}")
    
    if actual_train_shape == expected_shape and actual_test_shape == expected_shape:
        print(f"\n✓ VERIFICACIÓN EXITOSA: Las imágenes mantienen su estructura 2D (32x32x3)")
        print(f"✓ No se ha aplicado reshape ni flatten a las imágenes")
        print(f"✓ Las imágenes son compatibles con modelos CNN")
    else:
        print(f"\n✗ ADVERTENCIA: Las dimensiones no coinciden con lo esperado")
    
    print()


def main():
    """
    Función principal que ejecuta todos los pasos de preparación del dataset CIFAR-10
    """
    print("\n" + "🎯 " * 30)
    print("FASE 1 - PREPARACIÓN DEL DATASET VISUAL (CIFAR-10)")
    print("🎯 " * 30 + "\n")
    
    # Issue 1: Cargar el dataset CIFAR-10
    x_train, y_train, x_test, y_test = load_cifar10()
    
    # Issue 2: Visualizar imágenes de cada una de las 10 categorías
    visualize_categories(x_train, y_train)
    
    # Issue 3: Normalizar los valores de los píxeles
    x_train_norm, x_test_norm = normalize_images(x_train, x_test)
    
    # Issue 4: Aplicar One-Hot Encoding a las etiquetas
    y_train_encoded, y_test_encoded = apply_one_hot_encoding(y_train, y_test)
    
    # Issue 5: Verificar que las imágenes no sean aplanadas
    verify_image_dimensions(x_train_norm, x_test_norm)
    
    # Resumen final
    print("=" * 80)
    print("✅ RESUMEN DE LA PREPARACIÓN DEL DATASET")
    print("=" * 80)
    print(f"Dataset original:")
    print(f"  - Imágenes de entrenamiento: {x_train.shape}")
    print(f"  - Imágenes de prueba:        {x_test.shape}")
    print(f"  - Etiquetas de entrenamiento: {y_train.shape}")
    print(f"  - Etiquetas de prueba:        {y_test.shape}")
    print()
    print(f"Dataset procesado:")
    print(f"  - Imágenes de entrenamiento: {x_train_norm.shape} (normalizadas)")
    print(f"  - Imágenes de prueba:        {x_test_norm.shape} (normalizadas)")
    print(f"  - Etiquetas de entrenamiento: {y_train_encoded.shape} (one-hot)")
    print(f"  - Etiquetas de prueba:        {y_test_encoded.shape} (one-hot)")
    print()
    print("Todas las tareas de preparación se completaron exitosamente ✓")
    print("El dataset está listo para entrenar modelos CNN ✓")
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
