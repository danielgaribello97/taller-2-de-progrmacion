from modelos.Dispositivo import Dispositivo
from interfaces.IAutenticable import IAutenticable
from Encriptador import Encriptador # <--- Importar el encriptador

class ScannerBiometrico(Dispositivo, IAutenticable):
    def __init__(self, nombre, ubicacion, precision_minima):
        super().__init__(nombre, ubicacion)
        self.precision_minima = precision_minima
        # EJERCICIO 9: Composición (El scanner TIENE UN encriptador)
        self.encriptador = Encriptador() 

    def autenticar(self):
        print("Escaneando huella dactilar... [Análisis Biométrico]")
        return True

    def validar_acceso(self, empleado):
        print(f"Verificando huella de: {empleado.get_nombre()}")
        
        # Usamos la composición para cifrar el ID del empleado por seguridad
        id_cifrado = self.encriptador.cifrar_dato(empleado.get_id())
        print(f"ID del empleado protegido en logs: {id_cifrado}")

        if empleado.get_nivel_acceso() > 2:
            print(f"ACCESO CONCEDIDO en {self.ubicacion}")
            return True
        else:
            print(f"ACCESO DENEGADO: Nivel {empleado.get_nivel_acceso()} insuficiente.")
            return False