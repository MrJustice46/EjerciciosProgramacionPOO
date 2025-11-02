from Animal import Animal

class Caballo(Animal):
    def moverse(self):
        print("Camina, galopa y trota")

    def comunicacion(self):
        print("Se comunica con relinchos y movimientos")

    def alimentarse(self):
        print("Se alimenta de pasto y heno")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie")

    def adaptacion(self):
        print("Se adapta a climas templados y fríos")

    def instintos(self):
        print("Tiene instinto de huida ante el peligro")

    def descanso(self):
        print("Descansa de pie o echado")

    def sueño(self):
        print("Duerme 3 horas al dia")

    def interaccionSocial(self):
        print("Vive en grupos y sigue jerarquías")

    def imprimir(self):
        super().imprimir()