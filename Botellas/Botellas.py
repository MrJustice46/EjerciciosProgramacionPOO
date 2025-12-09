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
        
    def get(self):
        return self.color
    
    def get(self):
        return self.material
    
    def set(self, nuevoMaterial):
        self.material = nuevoMaterial
    
    def set(self, nuevoColor):
        self.color = nuevoColor
