from Carros import carros
from BaseDatos import BaseDatos
from Deportivo import Deportivo
from Van import Van
from Camion import Camion

#Codigo principal

print("DEPORTIVO")
ObjCarroDeportivo = Deportivo("Toyota Supra MK4", "Blanco", "2JZ-GTE", "3", "4", "Gasolina")
ObjCarroDeportivo2 = Deportivo("Ferrari F40", "Rojo", "V8 biturbo 2.9 litros.", "2", "2", "Gasolina")
ObjCarroDeportivo3 = Deportivo("Ford Mustang Shelby GT500", "Negro", "V8", "2", "4", "Gasolina")
print("\nVAN")
ObjCarroVan = Van("Ford Transit 150", "Negro", "V6 PFDI 3.5", "3", "15", "Gasolina")
ObjCarroVan2 = Van("Ford Tourneo Custom", "Negro", "Diésel EcoBlue", "5", "8", "Diesel")
print("\nCAMION")
ObjCarroCamion = Camion("Kenworth T600", "Negro", "ISX Cummins", "2", "2", "Diesel")
ObjCarroCamion2 = Camion("Mack 1977", "Blanco", "Motores Mack", "2", "2", "Diesel")

ObjBaseDatos = BaseDatos()

while True:
    print("""
        -------------- MENÚ ---------------- 
        1. Agregar vehiculos.
        2. Exntender lista.
        3. Insertar vehiculo.
        4. Eliminar vehiculos.
        5. Eliminar por posicion.
        6. Buscar por index.
        7. Contar vehiculos.
        8. ordenar lista.
        9. Invertir lista.
        10. Mostrar vehiculos
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
                1. Toyota Supra MK4
                2. Ford Transit 150
                """)
            try:
                Eleccion = int(input("Seleccione un vehiculo: "))
            
                match Eleccion:
                    case 1:
                        ObjBaseDatos.agregarDatos(ObjCarroDeportivo)
                        print("Toyota Supra MK4 agregado")
                    case 2:
                        ObjBaseDatos.agregarDatos(ObjCarroVan)
                        print("Ford Transit 150 agregado")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 2:
            print("""
                ------ VEHICULOS RESTANTES ------
                1. Kenworth T600
                2. Mack 1977
                3. Ferrari F40
                4. Agregar todas
                """)
            try:
                Seleccion_Extender = int(input("Seleccione una opción "))
                match Seleccion_Extender:
                    case 1:
                        ObjBaseDatos.extenderDatos([ObjCarroCamion])
                        print("Kenworth T600 agregado")
                    case 2:
                        ObjBaseDatos.extenderDatos([ObjCarroCamion2])
                        print(" mack 1977 agregado")
                    case 3:
                        ObjBaseDatos.extenderDatos([ObjCarroDeportivo2])
                        print("Ferrari F40 agregado")
                    case 4:
                        ObjBaseDatos.extenderDatos([ObjCarroCamion, ObjCarroCamion2, ObjCarroDeportivo2])
                        print("Todas los vehiculos agregados")
                    case _:
                        print("Ingrese una opción valida")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 3: 
            print("""
                ---------- VEHICULOS ----------
                1. Ford Mustang Shelby GT500
                2. Ford Tourneo Custom
            
                """)
            try: 
                EleccionInsertar = int(input("Ingrese una opción "))
                posicion = int(input("Ingrese la posicion del vehiculo: ")) - 1
                
                match EleccionInsertar:
                    case 1:
                        ObjBaseDatos.InsertarInfo(posicion, ObjCarroDeportivo3)
                        print(f"Ford Mustang Shelby GT500 insertado en la posicion {posicion+1}")
                    case 2:
                        ObjBaseDatos.InsertarInfo(posicion, ObjCarroVan2)
                        print(f"Ford Tourneo Custom insertado en la posicion {posicion+1}")
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
                ------ TODOS LOS VEHICULOS ------
                1. Toyota Supra MK4
                2. ford transit 150
                3. Kenworth T600
                4. Mack 1977
                5. Ferrari F40
                6. Ford Mustang Shelby GT500
                7. Ford Tourneo Custom
                """)
            try:
                seleccion_contar = int(input("Ingrese el vehiculo a mostrar: "))
                if len(ObjBaseDatos.lista) == 0:
                    print("No hay nada en la lista")
                else:
                    match seleccion_contar:
                        case 1:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroDeportivo)
                            print(f"Toyota Supra MK4 aparece {cantidad} veces")
                        case 2:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroVan)
                            print(f"ford transit 150 aparece {cantidad} veces")
                        case 3:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroCamion)
                            print(f"Kenworth T600 aparece {cantidad} veces")
                        case 4:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroCamion2)
                            print(f"Mack 1977 aparece {cantidad} veces")
                        case 5:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroDeportivo2)
                            print(f"Ferrari F40 aparece {cantidad} veces")
                        case 6:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroDeportivo3)
                            print(f"Ford Mustang Shelby GT500 aparece {cantidad} veces")
                        case 7:
                            cantidad = ObjBaseDatos.ContarInfo(ObjCarroVan2)
                            print(f"Ford Tourneo Custom aparece {cantidad} veces")
            except ValueError:
                print("Ingrese un numero valido")
        
        case 8: ObjBaseDatos.mostrar()
        case 9: ObjBaseDatos.InvertirInfo()
        case 10: ObjBaseDatos.ImprimirDatos()
        case _:
            print("Opcion no valida")
