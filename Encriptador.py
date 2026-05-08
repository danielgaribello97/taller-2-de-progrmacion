class Encriptador:
    def __init__(self, algoritmo="AES-256"):
        self.algoritmo = algoritmo

    def cifrar_dato(self, dato):
        # Una simulación de cifrado para el ejercicio
        print(f"Cifrando dato '{dato}' usando el algoritmo {self.algoritmo}...")
        return f"ENCRYPTED_{dato}_HASH"