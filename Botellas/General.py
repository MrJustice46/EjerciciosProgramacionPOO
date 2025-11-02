class Botella():
    
    def __init__(self, material, capacidad, forma):
        self.material = material 
        self.capacidad = capacidad 
        self.forma = forma

    def contenerLiquidos(self):
        print("contiene solo liquidos")
    
    def cierreHermetico(self):
        print("se cierra al vacio")
        
    def facilitarVertido(self):
        print("La forma facilita el vertido")
    
    def imprimir(self):
        print(f"material: {self.material}")
        print(f"capacidad: {self.capacidad}")
        print(f"forma: {self.forma}")
    
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

#Codigo principal
print("BOTELLA VIDRIO")
ObjBotellaVidrio = BotellaVidrio("vidrio", "2L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Marron")
ObjBotellaVidrio.imprimir()
ObjBotellaVidrio.contenerLiquidos()
ObjBotellaVidrio.cierreHermetico()
ObjBotellaVidrio.facilitarVertido()

print("\nBOTELLA PLASTICO")
ObjBotellaPlastico = BotellaPlastico("plastico", "1.5L", "Cilindrica", "con forma de botella", "Rosca", "Cristal", "Transparente")
ObjBotellaPlastico.imprimir()
ObjBotellaPlastico.contenerLiquidos()
ObjBotellaPlastico.cierreHermetico()
ObjBotellaPlastico.facilitarVertido()
