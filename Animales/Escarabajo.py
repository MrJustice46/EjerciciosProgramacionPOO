from Animal import Animal

class Escarabajo(Animal):
    def moverse(self):
        print("Camina y puede volar distancias cortas")

    def comunicacion(self):
        print("Usa vibraciones o feromonas para comunicarse")

    def alimentarse(self):
        print("Se alimenta de hojas o madera")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie, pone huevos en el suelo")

    def adaptacion(self):
        print("Se adapta a cualquier entorno")

    def instintos(self):
        print("Busca alimento y pareja por instinto, solo busca sobrevivir")

    def descanso(self):
        print("Descansa escondido bajo hojas o piedras")

    def sueño(self):
        print("Se queda inmovil para descansar, es lo mas cercano a dormir para ellos")

    def interaccionSocial(self):
        print("Es mayormente solitario, excepto en reproducción")

    def imprimir(self):
        super().imprimir()