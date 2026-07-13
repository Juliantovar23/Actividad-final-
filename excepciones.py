"""
Archivo: excepciones.py
Excepciones personalizadas del juego Cazador de Contraseñas.
"""


class LongitudInvalidaError(Exception):
    """Se genera cuando la longitud es menor que 8."""

    def __init__(self):
        super().__init__("La longitud debe ser mayor o igual a 8.")


class DatoNoNumericoError(Exception):
    """Se genera cuando el usuario no ingresa un número."""

    def __init__(self):
        super().__init__("Debe ingresar un valor numérico.")


class ContrasenaInvalidaError(Exception):
    """Se genera cuando la contraseña no cumple las reglas."""

    def __init__(self, mensaje):
        super().__init__(mensaje)