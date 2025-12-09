from Botellas import Botella
from BaseDatos import baseDatos
from BotellaVidrio import BotellaVidrio
from BotellaPlastico import BotellaPlastico

#Codigo principal
ObjBotellaVidrio = BotellaVidrio("vidrio", "1L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Marron")
ObjBotellaPlastico = BotellaPlastico("plastico", "1.5L", "Cilindrica", "con forma de botella", "Rosca", "Cristal", "Transparente")
ObjBotellaPlastico2 = BotellaPlastico("plastico", "2L", "Cilindrica", "con forma de botella", "Rosca", "Cristal", "Azul")
ObjBotellaPlastico3 = BotellaPlastico("plastico", "2.5L", "Cilindrica", "con forma de botella", "Rosca", "Cristal", "Rojo")
ObjBotellaVidrio2 = BotellaVidrio("vidrio", "3L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Marron")
ObjBotellaVidrio3 = BotellaVidrio("vidrio", "3.5L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Verde oscuro")
ObjBotellaVidrio4 = BotellaVidrio("vidrio", "4L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Verde")
ObjBotellaVidrio5 = BotellaVidrio("vidrio", "5L", "Bordelesa", "con forma de botella", "Corona", "Aguila", "Morado")

ObjBaseDatos = baseDatos()

while True:
    print("""
        -------------- MENÚ ---------------- 
        1. Agregar botellas
        2. Exntender lista.
        3. Insertar botella.
        4. Eliminar Botellas.
        5. Eliminar por posicion.
        6. Buscar por index.
        7. Contar botellas.
        8. ordenar lista.
        9. Invertir lista.
        10. Mostrar Botellas
        """)
    try:
        Respuesta = int(input("Ingrese un numero del menu "))
    except ValueError:
        print("Ingrese un numero valido")
        continue
    match Respuesta:
        case 1: 
            print("""
                ---------- BOTELLAS ---------
                1. Botella de plastico
                2. Botella de vidrio
                """)
            try:
                Eleccion = int(input("Seleccione una botella "))
            
                match Eleccion:
                    case 1:
                        ObjBaseDatos.agregarDatos(ObjBotellaPlastico)
                        print("Botella de plastico agregada")
                    case 2:
                        ObjBaseDatos.agregarDatos(ObjBotellaVidrio)
                        print("Botella de vidrio agregada")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 2:
            print("""
                ------ BOTELLAS RESTANTES ------
                1. Botella Plastico 2
                2. Botella Plastico 3
                3. Botella Vidrio 2
                4. Botella Vidrio 3
                5. Agregar todas
                """)
            try:
                Seleccion_Extender = int(input("Seleccione una opción "))
                match Seleccion_Extender:
                    case 1:
                        ObjBaseDatos.extenderDatos([ObjBotellaPlastico2])
                        print("Botella plastico 2 agregada")
                    case 2:
                        ObjBaseDatos.extenderDatos([ObjBotellaPlastico3])
                        print("Botella plastico 3 agregada")
                    case 3:
                        ObjBaseDatos.extenderDatos([ObjBotellaVidrio2])
                        print("Botella vidirio 2 agregada")
                    case 4:
                        ObjBaseDatos.extenderDatos([ObjBotellaVidrio3])
                        print("Botella vidrio 3 agregada")
                    case 5:
                        ObjBaseDatos.extenderDatos([ObjBotellaPlastico2, ObjBotellaPlastico3, ObjBotellaVidrio2, ObjBotellaVidrio3])
                        print("Todas las botellas agregadas")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 3: 
            print("""
                ----------BOTELLAS ----------
                1. Botella vidrio 4.
                2. Botella vidrio 5.
            
                """)
            try: 
                EleccionInsertar = int(input("Ingrese una opción "))
                posicion = int(input("Ingrese la posicion de la botella: ")) - 1
                
                match EleccionInsertar:
                    case 1:
                        ObjBaseDatos.InsertarInfo(posicion, ObjBotellaVidrio4)
                        print(f"Botella de vidrio 4 insertada en la posicion {posicion+1}")
                    case 2:
                        ObjBaseDatos.InsertarInfo(posicion, ObjBotellaVidrio5)
                        print(f"Botella de vidrio 5 insertada en la posicion {posicion+1}")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 4: 
            ObjBaseDatos.EliminarInfo()
        case 5: 
            ObjBaseDatos.EliminarInfoPosición()
        case 6:
            ObjBaseDatos.BuscarIndice()
        case 7: 
            print("""
                ------ TODAS LAS BOTELLAS ------ 
                1. Botella de plastico
                2. Botella de vidrio
                3. Botella Plastico 2
                4. Botella Plastico 3
                5. Botella Vidrio 2
                6. Botella Vidrio 3
                7. Botella vidrio 4.
                8. Botella vidrio 5.
                """)
            try:
                seleccion_contar = int(input("Ingrese la botella a mostrar: ")) 
                if len(ObjBaseDatos.lista) == 0:
                    print("No hay nada en la lista")
                else:
                    match seleccion_contar:
                        case 1:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaPlastico)
                            print(f"La botella de plástico aparece {cantidad} veces")
                        case 2:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaVidrio)
                            print(f"La botella de vidrio aparece {cantidad} veces")
                        case 3:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaPlastico2)
                            print(f"La botella de plástico 2 aparece {cantidad} veces")
                        case 4:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaPlastico3)
                            print(f"La botella de plástico 3 aparece {cantidad} veces")
                        case 5:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaVidrio2)
                            print(f"La botella de vidrio 2 aparece {cantidad} veces")
                        case 6:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaVidrio3)
                            print(f"La botella de vidrio 3 aparece {cantidad} veces")
                        case 7:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaVidrio4)
                            print(f"La botella de vidrio 4 aparece {cantidad} veces")
                        case 8:
                            cantidad = ObjBaseDatos.ContarInfo(ObjBotellaVidrio5)
                            print(f"La botella de vidrio 5 aparece {cantidad} veces")
                        case _:
                            print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 8:
            ObjBaseDatos.mostrar()
        case 9:
            ObjBaseDatos.InvertirInfo()
        case 10: ObjBaseDatos.ImprimirDatos()
        case _:
            print("Opcion no valida")
