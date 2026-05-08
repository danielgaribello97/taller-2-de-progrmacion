from modelos.Empleado import Empleado
from modelos.ScannerBiometrico import ScannerBiometrico
from core.Analizador import Analizador, AlertaSeguridadError

def ejecutar_sistema():
    # 1. Instancia de objetos (Ejercicio 1)
    empleado_normal = Empleado("Daniel Garibello", "DG-97", 3)
    intruso = Empleado("Desconocido", "XX-00", 0)
    
    scanner_principal = ScannerBiometrico("Scanner Frontal", "Entrada Principal", 98.5)
    analizador = Analizador()
    
    lista_dispositivos = [scanner_principal]
    
    try:
        # Prueba 1: Acceso exitoso
        analizador.procesar_intentos(lista_dispositivos, empleado_normal)
        
        # Prueba 2: Acceso sospechoso (esto disparará la excepción)
        analizador.procesar_intentos(lista_dispositivos, intruso)
        
    except AlertaSeguridadError as e:
        print(f"\n[SISTEMA DE BLOQUEO]: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_sistema()