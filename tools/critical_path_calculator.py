#!/usr/bin/env python3
"""
Calculadora de Ruta Crítica para el Proyecto de Rescate de Datos
Autor: Proyecto Rescate
Propósito: Ayudar a estudiantes a validar su análisis de ruta crítica
"""

def calcular_ruta_critica():
    """
    Calcula la ruta crítica del proyecto de rescate de datos
    """
    print("="*60)
    print("CALCULADORA DE RUTA CRÍTICA - RESCATE DE DATOS")
    print("="*60)
    
    # Definición de tareas
    tareas = {
        'A': {'descripcion': 'Identificar servidores afectados', 'duracion': 15, 'predecesoras': []},
        'B': {'descripcion': 'Priorizar datos críticos', 'duracion': 20, 'predecesoras': []},
        'C': {'descripcion': 'Activar protocolo de recuperación', 'duracion': 10, 'predecesoras': ['A']},
        'D': {'descripcion': 'Asignar técnicos a servidores', 'duracion': 5, 'predecesoras': ['B', 'C']},
        'E': {'descripcion': 'Recuperar datos de servidor 1', 'duracion': 30, 'predecesoras': ['D']},
        'F': {'descripcion': 'Recuperar datos de servidor 2', 'duracion': 25, 'predecesoras': ['E']},
        'G': {'descripcion': 'Validar integridad de datos', 'duracion': 15, 'predecesoras': ['E', 'F']},
        'H': {'descripcion': 'Generar informe preliminar', 'duracion': 10, 'predecesoras': ['G']},
        'I': {'descripcion': 'Comunicar a clientes afectados', 'duracion': 20, 'predecesoras': ['G']},
        'J': {'descripcion': 'Coordinar con equipo legal', 'duracion': 15, 'predecesoras': ['G']},
        'K': {'descripcion': 'Preparar plan de contingencia', 'duracion': 25, 'predecesoras': ['G']}
    }
    
    print("\n📋 TAREAS DEL PROYECTO:")
    print("-" * 80)
    for tarea, info in tareas.items():
        predecesoras_str = ', '.join(info['predecesoras']) if info['predecesoras'] else 'Ninguna'
        print(f"{tarea}: {info['descripcion']:<35} | {info['duracion']:2d} min | Pred: {predecesoras_str}")
    
    # Cálculo de tiempos tempranos (Early Start/Early Finish)
    tiempos_tempranos = {}
    
    def calcular_es_ef(tarea):
        if tarea in tiempos_tempranos:
            return tiempos_tempranos[tarea]
        
        info = tareas[tarea]
        if not info['predecesoras']:
            # Tarea sin predecesoras
            es = 0
            ef = es + info['duracion']
        else:
            # Tarea con predecesoras
            max_ef_predecesoras = 0
            for pred in info['predecesoras']:
                _, ef_pred = calcular_es_ef(pred)
                max_ef_predecesoras = max(max_ef_predecesoras, ef_pred)
            es = max_ef_predecesoras
            ef = es + info['duracion']
        
        tiempos_tempranos[tarea] = (es, ef)
        return (es, ef)
    
    # Calcular tiempos tempranos para todas las tareas
    for tarea in tareas.keys():
        calcular_es_ef(tarea)
    
    print("\n⏰ CÁLCULO DE TIEMPOS TEMPRANOS:")
    print("-" * 60)
    print("Tarea | Inicio Temprano | Fin Temprano | Duración")
    print("-" * 60)
    for tarea in sorted(tareas.keys()):
        es, ef = tiempos_tempranos[tarea]
        duracion = tareas[tarea]['duracion']
        print(f"  {tarea}   |      {es:3d}       |     {ef:3d}      |   {duracion:2d}")
    
    # Encontrar duración del proyecto
    tiempo_final = max(ef for es, ef in tiempos_tempranos.values())
    
    print(f"\n🎯 DURACIÓN TOTAL DEL PROYECTO: {tiempo_final} minutos")
    
    # Verificar restricción de 120 minutos
    if tiempo_final <= 120:
        print(f"✅ CUMPLE con el límite de 120 minutos (Margen: {120 - tiempo_final} min)")
    else:
        print(f"❌ EXCEDE el límite de 120 minutos (Sobrepaso: {tiempo_final - 120} min)")
    
    # Identificar ruta crítica
    print("\n🔍 IDENTIFICACIÓN DE RUTA CRÍTICA:")
    print("-" * 50)
    
    def encontrar_ruta_critica():
        # Calcular tiempos tardíos (Late Start/Late Finish)
        tiempos_tardios = {}
        
        # Empezar desde las tareas finales
        tareas_finales = []
        for tarea in tareas.keys():
            es_sucesor = False
            for otra_tarea, info in tareas.items():
                if tarea in info['predecesoras']:
                    es_sucesor = True
                    break
            if not es_sucesor:
                tareas_finales.append(tarea)
        
        def calcular_ls_lf(tarea):
            if tarea in tiempos_tardios:
                return tiempos_tardios[tarea]
            
            # Encontrar sucesoras
            sucesoras = []
            for otra_tarea, info in tareas.items():
                if tarea in info['predecesoras']:
                    sucesoras.append(otra_tarea)
            
            if not sucesoras:
                # Tarea final
                _, ef = tiempos_tempranos[tarea]
                lf = tiempo_final
                ls = lf - tareas[tarea]['duracion']
            else:
                # Tarea con sucesoras
                min_ls_sucesoras = float('inf')
                for suc in sucesoras:
                    ls_suc, _ = calcular_ls_lf(suc)
                    min_ls_sucesoras = min(min_ls_sucesoras, ls_suc)
                lf = min_ls_sucesoras
                ls = lf - tareas[tarea]['duracion']
            
            tiempos_tardios[tarea] = (ls, lf)
            return (ls, lf)
        
        # Calcular tiempos tardíos para todas las tareas
        for tarea in tareas.keys():
            calcular_ls_lf(tarea)
        
        # Identificar tareas críticas (holgura = 0)
        tareas_criticas = []
        for tarea in tareas.keys():
            es, ef = tiempos_tempranos[tarea]
            ls, lf = tiempos_tardios[tarea]
            holgura = ls - es
            if holgura == 0:
                tareas_criticas.append(tarea)
        
        return tareas_criticas, tiempos_tardios
    
    tareas_criticas, tiempos_tardios = encontrar_ruta_critica()
    
    print("\n📊 ANÁLISIS DE HOLGURAS:")
    print("-" * 80)
    print("Tarea | ES | EF | LS | LF | Holgura | ¿Crítica?")
    print("-" * 80)
    
    for tarea in sorted(tareas.keys()):
        es, ef = tiempos_tempranos[tarea]
        ls, lf = tiempos_tardios[tarea]
        holgura = ls - es
        critica = "SÍ" if tarea in tareas_criticas else "No"
        print(f"  {tarea}   |{es:3d} |{ef:3d} |{ls:3d} |{lf:3d} |   {holgura:2d}    |    {critica}")
    
    # Construir secuencia de ruta crítica
    print(f"\n🎯 RUTA CRÍTICA IDENTIFICADA:")
    print(f"Tareas críticas: {', '.join(sorted(tareas_criticas))}")
    
    # Reconstruir secuencia lógica de la ruta crítica
    ruta_secuencial = []
    tareas_procesadas = set()
    
    def agregar_a_ruta(tarea):
        if tarea in tareas_procesadas or tarea not in tareas_criticas:
            return
        
        # Primero agregar predecesoras críticas
        for pred in tareas[tarea]['predecesoras']:
            if pred in tareas_criticas:
                agregar_a_ruta(pred)
        
        if tarea not in tareas_procesadas:
            ruta_secuencial.append(tarea)
            tareas_procesadas.add(tarea)
    
    # Comenzar con tareas sin predecesoras críticas
    for tarea in tareas_criticas:
        agregar_a_ruta(tarea)
    
    print(f"Secuencia: {' → '.join(ruta_secuencial)}")
    
    # Calcular duración de la ruta crítica
    duracion_ruta_critica = sum(tareas[tarea]['duracion'] for tarea in ruta_secuencial)
    print(f"Duración de ruta crítica: {duracion_ruta_critica} minutos")
    
    # Análisis de optimización
    print("\n💡 ANÁLISIS DE OPTIMIZACIÓN:")
    print("-" * 50)
    print("• Las tareas A y B pueden ejecutarse en paralelo (no tienen dependencias)")
    print("• Esto permite ahorrar 15 minutos en la fase inicial")
    print("• Las tareas H, I, J, K pueden ejecutarse en paralelo después de G")
    print("• Se requieren 3 técnicos para optimizar el uso de recursos")
    
    # Verificar problemas potenciales
    print("\n⚠️  VERIFICACIÓN DE RESTRICCIONES:")
    print("-" * 50)
    
    # Verificar restricción de servidor único
    if tiempos_tempranos['F'][0] == tiempos_tempranos['E'][1]:
        print("✅ Restricción de servidor único respetada (F inicia cuando E termina)")
    else:
        print("❌ Error: F no inicia inmediatamente después de E")
    
    # Verificar dependencia de G
    tareas_post_g = ['H', 'I', 'J', 'K']
    inicio_g = tiempos_tempranos['G'][1]
    todas_correctas = all(tiempos_tempranos[tarea][0] >= inicio_g for tarea in tareas_post_g)
    
    if todas_correctas:
        print("✅ Restricción de validación respetada (H,I,J,K inician después de G)")
    else:
        print("❌ Error: Algunas tareas inician antes de completar G")
    
    print("\n" + "="*60)
    print("📚 Para más detalles, consulta la solución completa en:")
    print("    📁 solution/critical_path_analysis.md")
    print("="*60)

if __name__ == "__main__":
    calcular_ruta_critica()