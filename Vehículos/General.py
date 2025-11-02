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

#Codigo principal

print("DEPORTIVO")
ObjCarroDeportivo = Deportivo("Toyota Supra MK4", "Blanco", "2JZ-GTE", "3", "4", "Gasolina")
ObjCarroDeportivo.imprimir()
ObjCarroDeportivo.arranque()
ObjCarroDeportivo.acelerarFrenar()
ObjCarroDeportivo.direccion()
ObjCarroDeportivo.climatizacion()
ObjCarroDeportivo.Seguridad()
ObjCarroDeportivo.Luces()
ObjCarroDeportivo.SistemaVentanas()
ObjCarroDeportivo.SistemaEspejos()
ObjCarroDeportivo.apagado()

print("\nVAN")
ObjCarroVan = Van("Ford Transit 150", "Negro", "V6 PFDI 3.5", "3", "15", "Gasolina")
ObjCarroVan.imprimir()
ObjCarroVan.arranque()
ObjCarroVan.acelerarFrenar()
ObjCarroVan.direccion()
ObjCarroVan.climatizacion()
ObjCarroVan.Seguridad()
ObjCarroVan.Luces()
ObjCarroVan.SistemaVentanas()
ObjCarroVan.SistemaEspejos()
ObjCarroVan.apagado()

print("\nCAMION")
ObjCarroCamion = Camion("Kenworth T600", "Negro", "ISX Cummins", "2", "2", "Diesel")
ObjCarroCamion.imprimir()
ObjCarroCamion.arranque()
ObjCarroCamion.acelerarFrenar()
ObjCarroCamion.direccion()
ObjCarroCamion.climatizacion()
ObjCarroCamion.Seguridad()
ObjCarroCamion.Luces()
ObjCarroCamion.SistemaVentanas()
ObjCarroCamion.SistemaEspejos()
ObjCarroCamion.apagado()