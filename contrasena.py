

import random
import string

from excepciones import (
    LongitudInvalidaError,
    ContrasenaInvalidaError
)


class Contrasena:

    # Caracteres especiales permitidos por el enunciado
    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        self.longitud = longitud
        self.contrasena = ""

    def generar(self):


        # Validar longitud mínima
        if self.longitud < 8:
            raise LongitudInvalidaError()

        # Todos los caracteres disponibles
        caracteres = (
            string.ascii_letters +
            string.digits +
            self.CARACTERES_ESPECIALES
        )

        # Validar que existan suficientes caracteres únicos
        if self.longitud > len(caracteres):
            raise LongitudInvalidaError(
            )

        # Generar contraseña sin caracteres repetidos
        self.contrasena = "".join(
            random.sample(caracteres, self.longitud)
        )

        return self.contrasena

    def validar(self):


        if len(self.contrasena) < 8:
            raise ContrasenaInvalidaError(
                "La contraseña tiene menos de 8 caracteres."
            )

        # No debe tener caracteres repetidos
        if len(set(self.contrasena)) != len(self.contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña tiene caracteres repetidos."
            )

        # Debe contener una mayúscula
        if not any(c.isupper() for c in self.contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe contener al menos una letra mayúscula."
            )

        # Debe contener una minúscula
        if not any(c.islower() for c in self.contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe contener al menos una letra minúscula."
            )

        # Debe contener un número
        if not any(c.isdigit() for c in self.contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe contener al menos un número."
            )

        # Debe contener un carácter especial
        if not any(
            c in self.CARACTERES_ESPECIALES
            for c in self.contrasena
        ):
            raise ContrasenaInvalidaError(
                "La contraseña debe contener al menos un carácter especial."
            )

        return True

    def mostrar(self):

        print("\nContraseña generada:")
        print(self.contrasena)