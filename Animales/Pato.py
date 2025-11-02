from Animal import Animal

class Pato(Animal):
    def moverse(self):
        print("Camina, nada y puede volar")

    def comunicacion(self):
        print("Se comunica con graznidos o sonidos")

    def alimentarse(self):
        print("Se alimenta de plantas acuaticas, insectos pequeños y semillas")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie, pone huevos la hembra en un nido")

    def adaptacion(self):
        print("Tiene plumas impermeables para flotar y mantenerse seco, pueden adaptarse a diferentes climas")

    def instintos(self):
        print("Busca alimento y protege a sus crias por instinto")

    def descanso(self):
        print("Descansa en tierra o sobre el agua")

    def sueño(self):
        print("Duerme 10 horas al dia y suele dormir con un ojo abierto para vigilar su entorno")

    def interaccionSocial(self):
        print("Vive y migra en grupos")

    def imprimir(self):
        super().imprimir()