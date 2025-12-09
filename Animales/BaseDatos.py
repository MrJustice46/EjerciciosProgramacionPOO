class BaseDatos:
    def __init__(self):
        self.lista = []
        
    def agregarDatos(self, NuevoDato):
        self.lista.append(NuevoDato)
        print(f"{self.lista}")
        
    def extenderDatos(self, nuevaLista):
        self.lista.extend(nuevaLista)
        print(f"{self.lista}")
        
    def InsertarInfo(self, posicion, Animal):
        self.lista.insert(posicion, Animal)
        
    def EliminarInfo(self):
        if len(self.lista) == 0:
                print("No hay nada en la lista")
        else:
            cantidad = len(self.lista)
            while len(self.lista) > 0:
                self.lista.remove(self.lista[0])
            
            print(f"se eliminaron {cantidad} animales")
    
    def EliminarInfoPosición(self):
        if len(self.lista) == 0:
                print("No hay nada en la lista")
        else:
            self.ImprimirDatos()
            try:
                posicion = int(input("\nIngrese la posicion que desea eliminar: ")) - 1
                self.lista.pop(posicion)
                print(f"Animal #{posicion+1} eliminada correctamente")
            except ValueError:
                print("Error ingrese un numero valido")
    
    def BuscarIndiceInfo(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            self.mostrar()
            try:
                seleccion_index = int(input("Ingrese el vehiculo a mostrar: ")) -1 
                if 0 <= seleccion_index < len(self.lista):
                    self.ImprimirUnDato(self.lista[seleccion_index])
                else:
                    print("Numero fuera de rango")
            except ValueError:
                print("Error ingrese un numero valido")
    
    def ContarInfo(self, Animal):
        return self.lista.count(Animal) 
    
    def ordenar(self):
        self.lista.sort()
        
    def InvertirInfo(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            self.lista.reverse()
            print("Lista invertida")
    
    def buscar_por_nombre(self, nombre):
        for Animal in self.lista:
            if Animal.nombre == nombre:
                return Animal
            
    def BuscarIndice(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            nombre = input("Ingrese el nombre del animal: ")
            Animal = self.buscar_por_nombre(nombre)
            index = self.lista.index(Animal)
            print(f"\nAnimal #{index+1} encontrado")
            Animal.imprimir()

    def ImprimirUnDato(self, Animal):
        print(f"\Animal #{self.lista.index(Animal)+1}")
        Animal.imprimir()

    def ImprimirDatos(self):
        for i, Animal in enumerate(self.lista):
            print(f"\nAnimal #{i+1}")
            Animal.imprimir()

    def mostrar(self):
        for index in range(len(self.lista)):
            print(f"\Animal #{index+1}")

    