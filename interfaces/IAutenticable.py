from abc import ABC, abstractmethod

class IAutenticable(ABC):
    @abstractmethod
    def autenticar(self):
        """Método obligatorio para cualquier sistema de autenticación biométrica o PIN"""
        pass