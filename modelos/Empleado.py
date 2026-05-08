class Empleado:
    def __init__(self, nombre, id_empleado, nivel_acceso):
        # Ejercicio 2 y 3: Atributos privados e inicialización
        self.__nombre = nombre
        self.__id_empleado = id_empleado
        self.__nivel_acceso = nivel_acceso
        self.intentos_fallidos = 0

    # Getters para poder leer la información de forma segura
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id_empleado

    def get_nivel_acceso(self):
        return self.__nivel_acceso