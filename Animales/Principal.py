from Animal import Animal
from BaseDatos import BaseDatos
from Caballo import Caballo
from Cocodrilo import Cocodrilo
from Pez import Pez
from Escarabajo import Escarabajo
from Pato import Pato

#Codigo principal
ObjCaballo = Caballo("Caballo", "14 años", "heno", "llanura", "Mediano", "Blanco")
ObjCocodrilo = Cocodrilo("Cocodrilo", "30 años", "carne", "llanura", "Grande", "verde")
ObjPez = Pez("Pez", "2 años", "plancton", "rio", "Pequeño", "naranja")
ObjEscarabajo = Escarabajo("Escarabajo", "6 años", "hojas", "montaña", "Pequeño", "rojo")
ObjPato = Pato("Pato", "5 años", "plantas", "montaña", "Mediano", "Blanco")

Objbase = BaseDatos()

while True:
    print("""
        -------------- MENÚ ---------------- 
        1. Agregar animales.
        2. Exntender lista.
        3. Insertar animal.
        4. Eliminar Animales.
        5. Eliminar por posicion.
        6. Buscar por index.
        7. Contar animales.
        8. ordenar lista.
        9. Invertir lista.
        10. Mostrar animales
        """)
    try:
        Respuesta = int(input("Ingrese un numero del menu: "))
    except ValueError:
        print("Ingrese un numero valido")
        continue
    match Respuesta:
        case 1: 
            print("""
                ---------- ANIMALES ---------
                1. Caballo
                2. Cocodrilo
                """)
            try:
                Eleccion = int(input("Seleccione un animal: "))
            
                match Eleccion:
                    case 1:
                        Objbase.agregarDatos(ObjCaballo)
                        print("Caballo agregado")
                    case 2:
                        Objbase.agregarDatos(ObjCocodrilo)
                        print("Cocodrilo agregado")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 2:
            print("""
                ------ ANIMALES RESTANTES ------
                1. Pez
                2. Escarabajo
                3. Agregar todas
                """)
            try:
                Seleccion_Extender = int(input("Seleccione una opción "))
                match Seleccion_Extender:
                    case 1:
                        Objbase.extenderDatos([ObjPez])
                        print("pez agregado")
                    case 2:
                        Objbase.extenderDatos([ObjEscarabajo])
                        print(" escarabajo agregado")
                    case 3:
                        Objbase.extenderDatos([ObjPez, ObjEscarabajo])
                        print("Todos los animales agregados")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 3: 
            print("""
                ---------- ANIMALES ----------
                1. Pato
            
                """)
            try: 
                EleccionInsertar = int(input("Ingrese una opción "))
                posicion = int(input("Ingrese la posicion del animal: ")) - 1
                
                match EleccionInsertar:
                    case 1:
                        Objbase.InsertarInfo(posicion, ObjPato)
                        print(f"Pato insertado en la posicion {posicion+1}")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 4: 
            Objbase.EliminarInfo()
        case 5: 
            Objbase.EliminarInfoPosición()
        case 6:
            Objbase.BuscarIndice()
        case 7:
            print("""
                ------ TODOS LOS ANIMALES ------
                1. Caballo
                2. Cocodrilo
                3. Pez
                4. Escarabajo
                5. Pato
                """)
            try:
                seleccion_contar = int(input("Ingrese el animal a mostrar: ")) 
                if len(Objbase.lista) == 0:
                    print("No hay nada en la lista")
                else:
                    match seleccion_contar:
                        case 1:
                            cantidad = Objbase.ContarInfo(ObjCaballo)
                            print(f"Caballo aparece {cantidad} veces")
                        case 2:
                            cantidad = Objbase.ContarInfo(ObjCocodrilo)
                            print(f"Cocodrilo aparece {cantidad} veces")
                        case 3:
                            cantidad = Objbase.ContarInfo(ObjPez)
                            print(f"Pez aparece {cantidad} veces")
                        case 4:
                            cantidad = Objbase.ContarInfo(ObjEscarabajo)
                            print(f"Escarabajo aparece {cantidad} veces")
                        case 5:
                            cantidad = Objbase.ContarInfo(ObjPato)
                            print(f"Pato aparece {cantidad} veces")
                        case _:
                            print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 8: Objbase.ordenar()
        case 9: Objbase.InvertirInfo()
        case 10: Objbase.ImprimirDatos()
        case _:
            print("Opcion no valida")
