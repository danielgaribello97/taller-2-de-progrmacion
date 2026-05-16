from modelos.Empleado import Empleado
from modelos.ScannerBiometrico import ScannerBiometrico
from core.Analizador import Analizador, AlertaSeguridadError

def ejecutar_sistema():
    # Instancia de objetos para cada integrante del equipo
    integrante_1 = Empleado("Daniel Garibello", "DG-97", 3)
    integrante_2 = Empleado("Rosa Maria Marin", "RM-01", 3)
    integrante_3 = Empleado("Diana Atahualpa Zapata Villada", "DZ-02", 3)
    integrante_4 = Empleado("Diego Alejandro Gaviria Alzate", "DG-03", 3)
    
    # Instancia del usuario no autorizado para la prueba de bloqueo
    intruso = Empleado("Desconocido", "XX-00", 0)
    
    # Configuración del hardware y el analizador
    scanner_principal = ScannerBiometrico("Scanner Frontal", "Entrada Principal", 98.5)
    analizador = Analizador()
    
    lista_dispositivos = [scanner_principal]
    
    # Guardamos a todo el equipo en la lista para recorrerlo con el ciclo
    equipo_desarrollo = [integrante_1, integrante_2, integrante_3, integrante_4]
    
    try:
        # Procesamos de forma automática el acceso de cada miembro del grupo
        for integrante in equipo_desarrollo:
            analizador.procesar_intentos(lista_dispositivos, integrante)
        
        # Prueba con el intruso para hacer saltar la excepción de seguridad
        analizador.procesar_intentos(lista_dispositivos, intruso)
        
    except AlertaSeguridadError as e:
        print(f"\n[SISTEMA DE BLOQUEO]: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    ejecutar_sistema()