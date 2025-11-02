from Botellas import Botella

class BotellaPlastico(Botella):
    def __init__(self, material, capacidad, forma, diseño, Tapa, Grabado, color):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.tapa = Tapa
        self.color = color
        self.Grabado = Grabado

    def contenerLiquidos(self):
        print("contiene agua")

    def cierreHermetico(self):
        print("se cierra de rosca")

    def facilitarVertido(self):
        print("Su forma cilindrica facilita el vertido")

    def imprimir(self):
        super().imprimir()
        print(f"diseño: {self.diseño}")
        print(f"tapa: {self.tapa}")
        print(f"Grabado: {self.Grabado}")
        print(f"color: {self.color}")