from Animal import Animal

class Cocodrilo(Animal):
    def moverse(self):
        print("Se arrastra en tierra y nada en el agua")

    def comunicacion(self):
        print("Emite gruñidos y rugidos para comunicarse")

    def alimentarse(self):
        print("Se alimenta de carne y peces")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie y pone huevos en nidos cerca del agua")

    def adaptacion(self):
        print("Puede vivir tanto en agua dulce como salada")

    def instintos(self):
        print("Sus instintos son de supervivencia, caza por instinto y protege su territorio")

    def descanso(self):
        print("Descansa bajo el sol para mantener su temperatura")

    def sueño(self):
        print("Duerme entre 16 - 22 horas, con un ojo abierto para estar alerta")

    def interaccionSocial(self):
        print("Es solitario, solo se comunica y reune con su especie para aparearse")

    def imprimir(self):
        super().imprimir()