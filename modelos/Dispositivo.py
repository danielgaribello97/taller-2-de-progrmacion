class Dispositivo:
    def __init__(self, nombre_dispositivo, ubicacion):
        # Atributos comunes para todos los dispositivos
        self.nombre_dispositivo = nombre_dispositivo
        self.ubicacion = ubicacion

    def validar_acceso(self, empleado):
        """
        Método base que será sobreescrito por las clases hijas.
        Define la lógica general de validación.
        """
        print(f"Iniciando validación en {self.nombre_dispositivo} ({self.ubicacion})...")
        # Por defecto, una validación base no deja entrar a nadie hasta que
        # las clases hijas definan su lógica (Huella, PIN, etc.)
        return False