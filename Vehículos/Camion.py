from Carros import carros

class Camion(carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas)
        self.pasajeros = pasajeros
        self.combustible = combustible
    
    def arranque(self):
        print("arranca con fuerza, pero lento")

    def acelerarFrenar(self):
        print("acelera lentamente y requiere mas distancia para frenar")

    def direccion(self):
        print("tiene un sistema de direccion asistido por su peso")

    def climatizacion(self):
        print("Ventilacion basica en la cabina")

    def Seguridad(self):
        print("Cinturones de seguridad")

    def Luces(self):
        print("Luces potentes")

    def SistemaVentanas(self):
        print("Ventanas corredizas manuales")

    def SistemaEspejos(self):
        print("Espejos grandes")

    def apagado(self):
        print("Se apaga de forma lenta y ruidosa")

    def imprimir(self):
        super().imprimir()
        print(f"Numero de pasajeros: {self.pasajeros}")
        print(f"Combustible: {self.combustible}")