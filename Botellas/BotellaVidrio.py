from Botellas import Botella

class BotellaVidrio(Botella):
    def __init__(self, material, capacidad, forma, diseño, Tapa, Grabado, color):
        super().__init__(material, capacidad, forma)
        self.diseño = diseño
        self.tapa = Tapa
        self.Grabado = Grabado
        self.color = color

    def contenerLiquidos(self):
        print("Contiene cerveza")

    def cierreHermetico(self):
        print("Se cierra a presion")

    def facilitarVertido(self):
        print("Por su forma bordelesa, es un poco más dificil de verter")

    def imprimir(self):
        super().imprimir()
        print(f"diseño: {self.diseño}")
        print(f"tapa: {self.tapa}")
        print(f"Grabado: {self.Grabado}")
        print(f"color: {self.color}")