# Definimos una excepción personalizada para seguridad
class AlertaSeguridadError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Analizador:
    def __init__(self):
        self.historial_accesos = []

    def procesar_intentos(self, dispositivos, empleado):
        """
        Ejercicio 6: Polimorfismo. 
        Recibe una lista de dispositivos (pueden ser scanners, teclados, etc.)
        y procesa el acceso de forma genérica.
        """
        print(f"\n--- INICIANDO ANÁLISIS DE SEGURIDAD PARA: {empleado.get_nombre()} ---")
        
        for dispositivo in dispositivos:
            resultado = dispositivo.validar_acceso(empleado)
            self.historial_accesos.append(resultado)
            
            # Ejercicio 10: Lanzar excepción si el nivel es muy bajo (intento sospechoso)
            if empleado.get_nivel_acceso() < 1:
                raise AlertaSeguridadError(f"CRÍTICO: Intento de acceso de usuario no autorizado ID: {empleado.get_id()}")
            
        print("--- ANÁLISIS FINALIZADO SIN NOVEDADES CRÍTICAS ---")