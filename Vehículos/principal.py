from Carros import carros
from Deportivo import Deportivo
from Van import Van
from Camion import Camion

#Codigo principal

print("DEPORTIVO")
ObjCarroDeportivo = Deportivo("Toyota Supra MK4", "Blanco", "2JZ-GTE", "3", "4", "Gasolina")
ObjCarroDeportivo.imprimir()
ObjCarroDeportivo.arranque()
ObjCarroDeportivo.acelerarFrenar()
ObjCarroDeportivo.direccion()
ObjCarroDeportivo.climatizacion()
ObjCarroDeportivo.Seguridad()
ObjCarroDeportivo.Luces()
ObjCarroDeportivo.SistemaVentanas()
ObjCarroDeportivo.SistemaEspejos()
ObjCarroDeportivo.apagado()

print("\nVAN")
ObjCarroVan = Van("Ford Transit 150", "Negro", "V6 PFDI 3.5", "3", "15", "Gasolina")
ObjCarroVan.imprimir()
ObjCarroVan.arranque()
ObjCarroVan.acelerarFrenar()
ObjCarroVan.direccion()
ObjCarroVan.climatizacion()
ObjCarroVan.Seguridad()
ObjCarroVan.Luces()
ObjCarroVan.SistemaVentanas()
ObjCarroVan.SistemaEspejos()
ObjCarroVan.apagado()

print("\nCAMION")
ObjCarroCamion = Camion("Kenworth T600", "Negro", "ISX Cummins", "2", "2", "Diesel")
ObjCarroCamion.imprimir()
ObjCarroCamion.arranque()
ObjCarroCamion.acelerarFrenar()
ObjCarroCamion.direccion()
ObjCarroCamion.climatizacion()
ObjCarroCamion.Seguridad()
ObjCarroCamion.Luces()
ObjCarroCamion.SistemaVentanas()
ObjCarroCamion.SistemaEspejos()
ObjCarroCamion.apagado()