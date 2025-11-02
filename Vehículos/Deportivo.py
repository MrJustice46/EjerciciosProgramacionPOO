from Carros import carros

class Deportivo(carros):
    def __init__(self, modelo, color, motor, puertas, pasajeros, combustible):
        super().__init__(modelo, color, motor, puertas)
        self.pasajeros = pasajeros
        self.combustible = combustible

    def arranque(self):
        print("arranca con gran potencia")
        
    def acelerarFrenar(self):
        print("acelera muy rapido y frena con mucha precision")

    def direccion(self):
        print("tiene un sistema de direccion más directa y sensible")

    def climatizacion(self):
        print("El aire acondicionado es de alta calidad")

    def Seguridad(self):
        print("Cuenta con cinturones, frenos ABS y multiples airbags")

    def Luces(self):
        print("Cuenta con luces LED de alta calidad")

    def SistemaVentanas(self):
        print("Ventanas electricas automaticas")

    def SistemaEspejos(self):
        print("Espejos automáticos")
    
    def apagado(self):
        print("Se apaga muy rapido")
    
    def imprimir(self):
        super().imprimir()
        print(f"Numero de pasajeros: {self.pasajeros}")
        print(f"Combustible: {self.combustible}")