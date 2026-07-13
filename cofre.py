"""
Clase Cofre
Representa los diferentes tipos de cofres del juego.
"""

import random


class Cofre:

    def __init__(self):
        self.tipo = ""
        self.puntos = 0

    def abrir(self, contrasena_valida):
        """
        Si la contraseña es válida, abre un cofre aleatorio.
        Si es inválida, abre un cofre maldito.
        """

        if contrasena_valida:

            cofres = [
                ("Común", 10),
                ("Raro", 25),
                ("Legendario", 50)
            ]

            self.tipo, self.puntos = random.choice(cofres)

        else:

            self.tipo = "Maldito"
            self.puntos = -20

        return self.tipo, self.puntos

    def mostrar(self):
        """Muestra la información del cofre."""

        print("\n" + "=" * 35)
        print("COFRE OBTENIDO")
        print("=" * 35)
        print(f"Tipo   : {self.tipo}")
        print(f"Puntos : {self.puntos}")
        print("=" * 35)