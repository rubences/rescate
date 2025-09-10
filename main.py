"""
Programa de Rescate de Datos Críticos
Simulación de una situación de emergencia tecnológica con ataque de ransomware
Implementación usando Programación Orientada a Objetos (POO)
"""

from typing import List, Dict, Set
import heapq
from datetime import datetime, timedelta


class Task:
    """Clase que representa una tarea en el plan de rescate"""
    
    def __init__(self, task_id: str, name: str, duration: int, dependencies: List[str] = None, requires_technician: bool = True):
        """
        Constructor de la clase Task
        
        Args:
            task_id: Identificador único de la tarea (A, B, C, etc.)
            name: Nombre descriptivo de la tarea
            duration: Duración en minutos
            dependencies: Lista de tareas que deben completarse antes
            requires_technician: Si la tarea requiere un técnico disponible
        """
        self.task_id = task_id
        self.name = name
        self.duration = duration
        self.dependencies = dependencies or []
        self.requires_technician = requires_technician
        self.start_time = None
        self.end_time = None
        self.assigned_technician = None
        self.completed = False
        
    def can_start(self, completed_tasks: Set[str]) -> bool:
        """Verifica si la tarea puede iniciarse basado en dependencias completadas"""
        return all(dep in completed_tasks for dep in self.dependencies)
    
    def __str__(self):
        return f"Tarea {self.task_id}: {self.name} ({self.duration} min)"
    
    def __repr__(self):
        return self.__str__()


class Technician:
    """Clase que representa un técnico disponible para las tareas"""
    
    def __init__(self, technician_id: int):
        """
        Constructor de la clase Technician
        
        Args:
            technician_id: Identificador único del técnico
        """
        self.technician_id = technician_id
        self.available_time = 0  # Minuto en que estará disponible
        self.current_task = None
        
    def assign_task(self, task: Task, start_time: int):
        """Asigna una tarea al técnico"""
        self.current_task = task
        self.available_time = start_time + task.duration
        task.assigned_technician = self.technician_id
        
    def is_available(self, time: int) -> bool:
        """Verifica si el técnico está disponible en un momento dado"""
        return self.available_time <= time
    
    def __str__(self):
        return f"Técnico {self.technician_id} (disponible en minuto {self.available_time})"


class RescueManager:
    """Clase principal que gestiona toda la operación de rescate"""
    
    def __init__(self):
        """Constructor de la clase RescueManager"""
        self.tasks = {}
        self.technicians = [Technician(i+1) for i in range(3)]  # 3 técnicos disponibles
        self.timeline = []
        self.total_time_limit = 120  # 120 minutos límite
        self.completed_tasks = set()
        
        # Inicializar todas las tareas del rescate
        self._initialize_tasks()
        
    def _initialize_tasks(self):
        """Inicializa todas las tareas con sus dependencias y características"""
        task_definitions = [
            ("A", "Identificar servidores afectados", 15, [], True),
            ("B", "Priorizar datos críticos", 20, [], True),
            ("C", "Activar protocolo de recuperación", 10, ["A", "B"], True),
            ("D", "Asignar técnicos a servidores", 5, ["C"], True),
            ("E", "Recuperar datos de servidor 1", 30, ["D"], True),
            ("F", "Recuperar datos de servidor 2", 25, ["D"], True),
            ("G", "Validar integridad de datos recuperados", 15, ["E", "F"], True),
            ("H", "Generar informe preliminar para dirección", 10, ["G"], True),
            ("I", "Comunicar a clientes afectados", 20, ["G"], True),
            ("J", "Coordinar con equipo legal", 15, ["G"], True),
            ("K", "Preparar plan de contingencia", 25, ["G"], True),
        ]
        
        for task_id, name, duration, deps, needs_tech in task_definitions:
            self.tasks[task_id] = Task(task_id, name, duration, deps, needs_tech)
    
    def get_available_technician(self, time: int) -> Technician:
        """Encuentra el técnico que estará disponible más pronto"""
        available_techs = [tech for tech in self.technicians if tech.is_available(time)]
        if available_techs:
            return available_techs[0]
        
        # Si ninguno está disponible, devolver el que se libere más pronto
        return min(self.technicians, key=lambda t: t.available_time)
    
    def schedule_task(self, task: Task, current_time: int) -> int:
        """
        Programa una tarea para ejecutarse
        
        Args:
            task: La tarea a programar
            current_time: Tiempo actual en minutos
            
        Returns:
            Tiempo de finalización de la tarea
        """
        if task.requires_technician:
            technician = self.get_available_technician(current_time)
            start_time = max(current_time, technician.available_time)
            technician.assign_task(task, start_time)
        else:
            start_time = current_time
            
        task.start_time = start_time
        task.end_time = start_time + task.duration
        
        # Restricción especial: E y F deben ejecutarse secuencialmente
        if task.task_id == "F" and "E" in self.completed_tasks:
            task_e = self.tasks["E"]
            if task_e.end_time > start_time:
                task.start_time = task_e.end_time
                task.end_time = task.start_time + task.duration
                if task.requires_technician:
                    technician.available_time = task.end_time
        
        return task.end_time
    
    def create_rescue_plan(self) -> Dict:
        """
        Crea el plan de rescate optimizado usando programación de tareas con dependencias
        
        Returns:
            Diccionario con el plan completo y estadísticas
        """
        execution_order = []
        
        # Calcular tiempo de inicio más temprano para cada tarea
        earliest_start = {}
        
        # Función recursiva para calcular el tiempo más temprano de inicio
        def calculate_earliest_start(task_id):
            if task_id in earliest_start:
                return earliest_start[task_id]
            
            task = self.tasks[task_id]
            if not task.dependencies:
                earliest_start[task_id] = 0
            else:
                max_dep_end = 0
                for dep_id in task.dependencies:
                    dep_start = calculate_earliest_start(dep_id)
                    dep_end = dep_start + self.tasks[dep_id].duration
                    max_dep_end = max(max_dep_end, dep_end)
                earliest_start[task_id] = max_dep_end
            
            return earliest_start[task_id]
        
        # Calcular tiempos de inicio más tempranos para todas las tareas
        for task_id in self.tasks:
            calculate_earliest_start(task_id)
        
        # Aplicar restricción especial: F debe empezar después de E
        earliest_start["F"] = max(earliest_start["F"], 
                                 earliest_start["E"] + self.tasks["E"].duration)
        
        # Recalcular dependencias que dependen de F después de la restricción
        if "G" in self.tasks and "F" in self.tasks["G"].dependencies:
            earliest_start["G"] = max(earliest_start["G"],
                                     earliest_start["F"] + self.tasks["F"].duration)
        
        # Ordenar tareas por tiempo de inicio más temprano
        task_schedule = sorted(self.tasks.items(), 
                              key=lambda x: (earliest_start[x[0]], x[1].duration))
        
        # Programar cada tarea
        for task_id, task in task_schedule:
            start_time = earliest_start[task_id]
            
            # Encontrar técnico disponible
            if task.requires_technician:
                technician = self.get_available_technician(start_time)
                actual_start = max(start_time, technician.available_time)
                technician.assign_task(task, actual_start)
            else:
                actual_start = start_time
            
            task.start_time = actual_start
            task.end_time = actual_start + task.duration
            task.completed = True
            execution_order.append(task)
            self.completed_tasks.add(task_id)
        
        # Calcular el tiempo total
        total_time = max(task.end_time for task in self.tasks.values())
        
        return {
            "execution_order": sorted(execution_order, key=lambda t: t.start_time),
            "total_time": total_time,
            "completed_tasks": len(self.completed_tasks),
            "total_tasks": len(self.tasks),
            "success": len(self.completed_tasks) == len(self.tasks) and total_time <= self.total_time_limit
        }
    
    def print_rescue_plan(self, plan: Dict):
        """Imprime el plan de rescate de manera clara y organizada"""
        print("=" * 80)
        print("🚨 PLAN DE RESCATE DE DATOS CRÍTICOS 🚨")
        print("=" * 80)
        print(f"⏰ Tiempo límite: {self.total_time_limit} minutos")
        print(f"👥 Técnicos disponibles: {len(self.technicians)}")
        print(f"📋 Total de tareas: {plan['total_tasks']}")
        print()
        
        if plan["success"]:
            print("✅ PLAN FACTIBLE - Todas las tareas pueden completarse a tiempo")
        else:
            print("❌ PLAN CRÍTICO - No todas las tareas pueden completarse")
        
        print(f"⏱️  Tiempo total estimado: {plan['total_time']} minutos")
        print(f"✓ Tareas completadas: {plan['completed_tasks']}/{plan['total_tasks']}")
        print()
        
        print("📊 CRONOGRAMA DE EJECUCIÓN:")
        print("-" * 80)
        print(f"{'Tarea':<6} {'Descripción':<40} {'Inicio':<7} {'Fin':<7} {'Técnico':<8}")
        print("-" * 80)
        
        for task in plan["execution_order"]:
            tech_str = f"T{task.assigned_technician}" if task.assigned_technician else "N/A"
            print(f"{task.task_id:<6} {task.name:<40} {task.start_time:<7} {task.end_time:<7} {tech_str:<8}")
        
        print("-" * 80)
        
        # Mostrar utilización de recursos
        print("\n📈 UTILIZACIÓN DE RECURSOS:")
        for tech in self.technicians:
            utilization = (tech.available_time / self.total_time_limit) * 100
            print(f"Técnico {tech.technician_id}: {tech.available_time} min trabajados ({utilization:.1f}% utilización)")
        
        # Mostrar dependencias críticas
        print("\n🔗 DEPENDENCIAS CRÍTICAS:")
        for task_id, task in self.tasks.items():
            if task.dependencies:
                deps_str = " → ".join(task.dependencies)
                print(f"{deps_str} → {task_id}")
    
    def generate_communication_plan(self):
        """Genera el plan de comunicación de crisis"""
        print("\n" + "=" * 80)
        print("📢 PLAN DE COMUNICACIÓN DE CRISIS")
        print("=" * 80)
        
        stakeholders = [
            "👔 Dirección ejecutiva: Informe cada 30 minutos",
            "⚕️  Clientes (hospitales): Comunicación tras validación de datos",
            "⚖️  Equipo legal: Coordinación inmediata post-validación",
            "🛡️ Equipo de seguridad: Monitoreo continuo",
            "💻 Personal técnico: Briefing cada 15 minutos"
        ]
        
        for stakeholder in stakeholders:
            print(f"• {stakeholder}")


def main():
    """Función principal del programa"""
    print("Iniciando simulación de rescate de datos críticos...")
    print()
    
    # Crear el gestor de rescate
    rescue_manager = RescueManager()
    
    # Crear el plan de rescate
    plan = rescue_manager.create_rescue_plan()
    
    # Mostrar el plan completo
    rescue_manager.print_rescue_plan(plan)
    
    # Mostrar plan de comunicación
    rescue_manager.generate_communication_plan()
    
    print("\n" + "=" * 80)
    if plan["success"]:
        print("🎯 MISIÓN POSIBLE: El rescate puede completarse exitosamente")
    else:
        print("⚠️  MISIÓN CRÍTICA: Se requiere optimización adicional")
    print("=" * 80)


if __name__ == "__main__":
    main()