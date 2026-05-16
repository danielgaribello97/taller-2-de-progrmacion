class Empleado:
    def __init__(self, nombre, id_empleado, nivel_acceso):
        # Atributos privados para cumplir con el encapsulamiento seguro
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__nivel_acceso = nivel_acceso
        self.intentos_fallidos = 0

    # Getters públicos para permitir la lectura controlada de datos
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id_empleado

    def get_nivel_acceso(self):
        return self.__nivel_acceso