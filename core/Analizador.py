class AlertaSeguridadError(Exception):
    """Excepción personalizada para interceptar amenazas e intentos de intrusión"""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Analizador:
    def __init__(self):
        self.historial_accesos = []

    def procesar_intentos(self, dispositivos, empleado):
        """
        Aplica Polimorfismo al recibir una lista genérica de dispositivos 
        y procesar la validación sin importar el tipo de hardware exacto.
        """
        print(f"\n--- INICIANDO ANÁLISIS DE SEGURIDAD PARA: {empleado.get_nombre()} ---")
        
        for dispositivo in dispositivos:
            resultado = dispositivo.validar_acceso(empleado)
            self.historial_accesos.append(resultado)
            
            # Lanzamiento de excepción si el usuario carece de nivel mínimo (Políticas de Zero-Trust)
            if empleado.get_nivel_acceso() < 1:
                raise AlertaSeguridadError(f"CRÍTICO: Intento de violación de perímetro por usuario ID: {empleado.get_id()}")
            
        print("--- ANÁLISIS FINALIZADO SIN NOVEDADES CRÍTICAS ---")