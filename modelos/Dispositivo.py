class Dispositivo:
    def __init__(self, nombre_dispositivo, ubicacion):
        # Atributos comunes para todos los dispositivos
        self.nombre_dispositivo = nombre_dispositivo
        self.ubicacion = ubicacion

    def validar_acceso(self, empleado):
        """
        Método base diseñado para ser sobreescrito por las clases hijas (Polimorfismo).
        """
        print(f"Iniciando validación en {self.nombre_dispositivo} ({self.ubicacion})...")
        return False