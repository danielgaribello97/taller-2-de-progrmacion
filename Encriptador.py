class Encriptador:
    def __init__(self, algoritmo="AES-256"):
        self.algoritmo = algoritmo

    def cifrar_dato(self, dato):
        # Simulación del proceso de hashing/cifrado para la lógica de auditoría
        print(f"Cifrando dato '{dato}' usando el algoritmo {self.algoritmo}...")
        return f"ENCRYPTED_{dato}_HASH"