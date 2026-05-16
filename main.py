from modelos.Empleado import Empleado
from modelos.ScannerBiometrico import ScannerBiometrico
from core.Analizador import Analizador, AlertaSeguridadError

def ejecutar_sistema():
    # 1. Instancia de objetos para cada integrante del equipo (Requerimiento de la guía)
    integrante_1 = Empleado("Daniel Garibello", "DG-97", 3)
    integrante_2 = Empleado("Rosa Maria Marin", "RM-01", 3)
    
    # Instancia de un usuario no autorizado para simular la brecha
    intruso = Empleado("Desconocido", "XX-00", 0)
    
    # Configuración del hardware perimetral y el analizador
    scanner_principal = ScannerBiometrico("Scanner Frontal", "Entrada Principal", 98.5)
    analizador = Analizador()
    
    lista_dispositivos = [scanner_principal]
    
    # Agrupamos al equipo de trabajo en una lista para procesarlos dinámicamente
    equipo_desarrollo = [integrante_1, integrante_2]
    
    try:
        # PRUEBA 1: Acceso exitoso para todos los integrantes autorizados del grupo
        for integrante in equipo_desarrollo:
            analizador.procesar_intentos(lista_dispositivos, integrante)
        
        # PRUEBA 2: Acceso sospechoso (Esto disparará la excepción de seguridad)
        analizador.procesar_intentos(lista_dispositivos, intruso)
        
    except AlertaSeguridadError as e:
        print(f"\n[SISTEMA DE BLOQUEO]: {e}")
    except Exception as e:
        print(f"Error inesperado en el sistema: {e}")

if __name__ == "__main__":
    ejecutar_sistema()