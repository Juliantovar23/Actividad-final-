from contrasena import Contrasena
from cofre import Cofre
from excepciones import (
    LongitudInvalidaError,
    DatoNoNumericoError,
    ContrasenaInvalidaError
)

class JuegoCazador:

    def __init__(self):
        self.puntaje = 0
        self.ronda = 1

    def jugar(self):

        print("=" * 50)
        print("      CAZADOR DE CONTRASEÑAS")
        print("=" * 50)

        while True:

            print(f"\nRonda {self.ronda}")

            try:

                entrada = input("Ingrese la longitud de la contraseña: ")

                if not entrada.isdigit():
                    raise DatoNoNumericoError()

                longitud = int(entrada)

                contrasena = Contrasena(longitud)

                texto = contrasena.generar()

                print("\nContraseña generada:")
                print(texto)

                contrasena.validar()

                print("\n✅ Contraseña válida")

                cofre = Cofre()

                tipo, puntos = cofre.abrir(True)

            except LongitudInvalidaError as error:

                print("\n❌", error)

                tipo, puntos = Cofre().abrir(False)

            except DatoNoNumericoError as error:

                print("\n❌", error)

                tipo, puntos = Cofre().abrir(False)

            except ContrasenaInvalidaError as error:

                print("\n❌", error)

                tipo, puntos = Cofre().abrir(False)

            self.puntaje += puntos

            print("\n" + "-" * 35)
            print("Resultado")
            print("-" * 35)
            print("Tipo de cofre :", tipo)
            print("Puntos ronda  :", puntos)
            print("Puntaje total :", self.puntaje)

            continuar = input(
                "\n¿Desea jugar otra ronda? (S/N): "
            ).upper()

            while continuar not in ("S", "N"):

                continuar = input(
                    "Ingrese únicamente S o N: "
                ).upper()

            if continuar == "N":

                print("\nJuego terminado.")
                print("Puntaje final:", self.puntaje)

                break

            self.ronda += 1