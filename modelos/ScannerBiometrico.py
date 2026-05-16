from modelos.Dispositivo import Dispositivo
from interfaces.IAutenticable import IAutenticable
from Encriptador import Encriptador

class ScannerBiometrico(Dispositivo, IAutenticable):
    def __init__(self, nombre, ubicacion, precision_minima):
        # Invocación al constructor de la clase padre (Herencia)
        super().__init__(nombre, ubicacion)
        self.precision_minima = precision_minima
        
        # Composición: El scanner contiene y depende de un Encriptador
        self.encriptador = Encriptador() 

    def autenticar(self):
        print("Escaneando huella dactilar... [Análisis Biométrico]")
        return True

    def validar_acceso(self, empleado):
        print(f"Verificando credenciales biometricas de: {empleado.get_nombre()}")
        
        # Uso de la composición para proteger el ID del empleado en logs haseados
        id_cifrado = self.encriptador.cifrar_dato(empleado.get_id())
        print(f"ID de empleado protegido en registros logs: {id_cifrado}")

        if empleado.get_nivel_acceso() > 2:
            print(f"ACCESO CONCEDIDO en la ubicación: {self.ubicacion}")
            return True
        else:
            print(f"ACCESO DENEGADO: Nivel de privilegios ({empleado.get_nivel_acceso()}) insuficientes.")
            return False