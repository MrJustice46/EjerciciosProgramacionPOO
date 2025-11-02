class carros():
    def __init__(self, modelo, color, motor, puertas):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.puertas = puertas
        
    def arranque(self):
        print("el carro arranca")

    def acelerarFrenar(self):
        print("el carro acelera y frena")
    
    def direccion(self):
        print("el sistema de dirrecion funciona correctamente")

    def climatizacion(self):
        print("El sistema de climatización mantiene la temperatura adecuada")

    def Seguridad(self):
        print("el carro cuenta con cinturones y airbags")

    def Luces(self):
        print("las luces funcionan correctamente")

    def SistemaVentanas(self):
        print("el sistema de ventanas funciona correctamente")

    def SistemaEspejos(self):
        print("los espejos estan bien colocados")

    def apagado(self):
        print("el carro se ha apagado")
    
    def imprimir(self):
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Numero de puertas: {self.puertas}")