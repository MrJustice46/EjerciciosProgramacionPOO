class Animal():
    def __init__(self, nombre, edad, dieta, habitat, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.dieta = dieta
        self.habitat = habitat
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print("el animal se mueve")

    def comunicacion(self):
        print("el animal se comunica con sonidos y gestos")

    def reproduccion(self):
        print("el animal se reproduce segun su especie")

    def alimentarse(self):
        print("el animal se alimenta")

    def adaptacion(self):
        print("el animal se adapta a su entorno")

    def instintos(self):
        print("el animal actua por instintos")

    def descanso(self):
        print("el animal descansa")

    def sueño(self):
        print("el animal duerme por periodos")

    def interaccionSocial(self):
        print("el animal interactua con otros animales")

    def imprimir(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"dieta: {self.dieta}")
        print(f"habitat: {self.habitat}")
        print(f"tamaño: {self.tamaño}")
        print(f"color: {self.color}")