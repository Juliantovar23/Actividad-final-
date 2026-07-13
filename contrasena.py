"""
Clase Contrasena
Genera y valida contraseñas aleatorias.
"""

import random
import string

from excepciones import (
    LongitudInvalidaError,
    ContrasenaInvalidaError
)


class Contrasena:

    CARACTERES_ESPECIALES = "¿¡?=)(/¨*+-%&$#!"

    def __init__(self, longitud):
        self.longitud = longitud
        self.contrasena = ""

    def generar(self):
        """
        Genera una contraseña completamente aleatoria.
        """

        if self.longitud < 8:
            raise LongitudInvalidaError()

        caracteres = (
            string.ascii_letters +
            string.digits +
            self.CARACTERES_ESPECIALES
        )

        self.contrasena = ""

        for _ in range(self.longitud):
            self.contrasena += random.choice(caracteres)

        return self.contrasena

    def validar(self):
        """
        Verifica que la contraseña cumpla todas las condiciones.
        """

        texto = self.contrasena

        if len(texto) < 8:
            raise ContrasenaInvalidaError(
                "La contraseña tiene menos de 8 caracteres."
            )

        if len(set(texto)) != len(texto):
            raise ContrasenaInvalidaError(
                "La contraseña tiene caracteres repetidos."
            )

        if not any(c.isupper() for c in texto):
            raise ContrasenaInvalidaError(
                "Debe contener al menos una letra mayúscula."
            )

        if not any(c.islower() for c in texto):
            raise ContrasenaInvalidaError(
                "Debe contener al menos una letra minúscula."
            )

        if not any(c.isdigit() for c in texto):
            raise ContrasenaInvalidaError(
                "Debe contener al menos un número."
            )

        if not any(
            c in self.CARACTERES_ESPECIALES
            for c in texto
        ):
            raise ContrasenaInvalidaError(
                "Debe contener al menos un carácter especial."
            )

        return True