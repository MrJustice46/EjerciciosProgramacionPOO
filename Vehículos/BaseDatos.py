class baseDatos:
    def __init__(self):
        self.lista = []
        
    def agregarDatos(self, newBotella):
        self.lista.append(newBotella)
        print(f"{self.lista}")
        
    def extenderDatos(self, nuevaLista):
        self.lista.extend(nuevaLista)
        
    def InsertarInfo(self, posicion, botella):
        self.lista.insert(posicion, botella)
        
    def EliminarInfo(self):
        if len(self.lista) == 0:
                print("No hay nada en la lista")
        else:
            cantidad = len(self.lista)
            while len(self.lista) > 0:
                self.lista.remove(self.lista[0])
            
            print(f"se eliminaron {cantidad} botellas")
    
    def EliminarInfoPosición(self):
        if len(self.lista) == 0:
                print("No hay nada en la lista")
        else:
            self.ImprimirDatos()
            try:
                posicion = int(input("\nIngrese la posicion que desea eliminar: ")) - 1
                self.lista.pop(posicion)
                print(f"Botella #{posicion+1} eliminada correctamente")
            except ValueError:
                print("Error ingrese un numero valido")
    
    def BuscarIndiceInfo(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            self.mostrar()
            try:
                seleccion_index = int(input("Ingrese la botella a mostrar: ")) -1 
                if 0 <= seleccion_index < len(self.lista):
                    self.ImprimirUnDato(self.lista[seleccion_index])
                else:
                    print("Numero fuera de rango")
            except ValueError:
                print("Error ingrese un numero valido")
    
    def ContarInfo(self, botella):
        return self.lista.count(botella) 
        
    def InvertirInfo(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            self.lista.reverse()
            print("Lista invertida")
    
    def buscar_por_capacidad(self, capacidad):
        for botella in self.lista:
            if botella.capacidad == capacidad:
                return botella
            
    def BuscarIndice(self):
        if len(self.lista) == 0:
            print("No hay nada en la lista")
        else:
            capacidad = input("Ingrese la capacidad de la botella: ")
            Botella = self.buscar_por_capacidad(capacidad)
            index = self.lista.index(Botella)
            print(f"\nBotella #{index+1} encontrada")
            Botella.imprimir()

    def ImprimirUnDato(self, Botella):
        print(f"\nBotella #{self.lista.index(Botella)+1}")
        Botella.imprimir()

    def ImprimirDatos(self):
        for i, Botella in enumerate(self.lista):
            print(f"\nBotella #{i+1}")
            Botella.imprimir()

    def mostrar(self):
        for index in range(len(self.lista)):
            print(f"\nBotella #{index+1}")                           



