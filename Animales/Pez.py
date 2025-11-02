from Animal import Animal

class Pez(Animal):
    def moverse(self):
        print("Nada moviendo sus aletas y cola.")

    def comunicacion(self):
        print("Se comunica con movimientos, sonidos y cambios de color")

    def alimentarse(self):
        print("Se alimenta de plancton o pequeños organismos.")

    def reproduccion(self):
        print("Pone huevos en el agua, fecundacion externa entre el macho y la hembra")

    def adaptacion(self):
        print("El pez respira oxígeno del agua mediante branquias y una forma de cuerpo aerodinámico")

    def instintos(self):
        print("Tiene instinto de supervivencia pasivo, huye de depredadores y busca alimento por instinto")

    def descanso(self):
        print("Reduce su actividad para descansar")

    def sueño(self):
        print("Duerme entre 8 - 12 horas flotando sin cerrar los ojos.")

    def interaccionSocial(self):
        print("Nada en grupos llamados bancos entre peces")

    def imprimir(self):
        super().imprimir()