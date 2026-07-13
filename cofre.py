
import random


class Cofre:

    def __init__(self):
        self.tipo = ""
        self.puntos = 0

    def abrir(self, contrasena_valida):


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

        print("\n" + "=" * 35)
        print("COFRE OBTENIDO")
        print("=" * 35)
        print(f"Tipo   : {self.tipo}")
        print(f"Puntos : {self.puntos}")
        print("=" * 35)