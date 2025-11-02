from Carros import carros

class Van(carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas)
        self.pasajeros = pasajeros
        self.combustible = combustible

    def arranque(self):
        print("arranca de forma suave y lenta")

    def acelerarFrenar(self):
        print("acelera lentamente y frena con suavidad")

    def direccion(self):
        print("tiene un sistema de direccion estable y comodo")

    def climatizacion(self):
        print("Cuenta con aire acondicionado basico")

    def Seguridad(self):
        print("Tiene cinturones de seguriddad en todos los asientos")

    def Luces(self):
        print("Tiene luces delanteras y traseras comunes")

    def SistemaVentanas(self):
        print("Ventanas corredizas manuales")

    def SistemaEspejos(self):
        print("Espejos laterales amplios")

    def apagado(self):
        print("se apaga de forma lenta y silenciosa")

    def imprimir(self):
        super().imprimir()
        print(f"Numero de pasajeros: {self.pasajeros}")
        print(f"Combustible: {self.combustible}")