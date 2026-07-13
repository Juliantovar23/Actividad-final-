class LongitudInvalidaError(Exception):


    def __init__(self):
        super().__init__("La longitud debe ser mayor o igual a 8.")


class DatoNoNumericoError(Exception):

    def __init__(self):
        super().__init__("Debe ingresar un valor numérico.")


class ContrasenaInvalidaError(Exception):

    def __init__(self, mensaje):
        super().__init__(mensaje)