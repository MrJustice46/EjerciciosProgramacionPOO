class Animal():
    def __init__(self, nombre, edad, dieta, habitat, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.dieta = dieta
        self.habitat = habitat
        self.tamaño = tamaño
        self.color = color

    def moverse(self):
        print("el animal se mueve")

    def comunicacion(self):
        print("el animal se comunica con sonidos y gestos")

    def reproduccion(self):
        print("el animal se reproduce segun su especie")

    def alimentarse(self):
        print("el animal se alimenta")

    def adaptacion(self):
        print("el animal se adapta a su entorno")

    def instintos(self):
        print("el animal actua por instintos")

    def descanso(self):
        print("el animal descansa")

    def sueño(self):
        print("el animal duerme por periodos")

    def interaccionSocial(self):
        print("el animal interactua con otros animales")

    def imprimir(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad}")
        print(f"dieta: {self.dieta}")
        print(f"habitat: {self.habitat}")
        print(f"tamaño: {self.tamaño}")
        print(f"color: {self.color}")

class Caballo(Animal):
    def moverse(self):
        print("Camina, galopa y trota")

    def comunicacion(self):
        print("Se comunica con relinchos y movimientos")

    def alimentarse(self):
        print("Se alimenta de pasto y heno")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie")

    def adaptacion(self):
        print("Se adapta a climas templados y fríos")

    def instintos(self):
        print("Tiene instinto de huida ante el peligro")

    def descanso(self):
        print("Descansa de pie o echado")

    def sueño(self):
        print("Duerme 3 horas al dia")

    def interaccionSocial(self):
        print("Vive en grupos y sigue jerarquías")

    def imprimir(self):
        super().imprimir()

class Cocodrilo(Animal):
    def moverse(self):
        print("Se arrastra en tierra y nada en el agua")

    def comunicacion(self):
        print("Emite gruñidos y rugidos para comunicarse")

    def alimentarse(self):
        print("Se alimenta de carne y peces")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie y pone huevos en nidos cerca del agua")

    def adaptacion(self):
        print("Puede vivir tanto en agua dulce como salada")

    def instintos(self):
        print("Sus instintos son de supervivencia, caza por instinto y protege su territorio")

    def descanso(self):
        print("Descansa bajo el sol para mantener su temperatura")

    def sueño(self):
        print("Duerme entre 16 - 22 horas, con un ojo abierto para estar alerta")

    def interaccionSocial(self):
        print("Es solitario, solo se comunica y reune con su especie para aparearse")

    def imprimir(self):
        super().imprimir()

class Pez(Animal):
    def moverse(self):
        print("Nada moviendo sus aletas y cola.")

    def comunicacion(self):
        print("Se comunica con movimientos, sonidos y cambios de color")

    def alimentarse(self):
        print("Se alimenta de plancton o pequeños organismos.")

    def reproduccion(self):
        print("Pone huevos en el agua, fecundacion externa entre el macho y la hembra")

    def adaptacion(self):
        print("El pez respira oxígeno del agua mediante branquias y una forma de cuerpo aerodinámico")

    def instintos(self):
        print("Tiene instinto de supervivencia pasivo, huye de depredadores y busca alimento por instinto")

    def descanso(self):
        print("Reduce su actividad para descansar")

    def sueño(self):
        print("Duerme entre 8 - 12 horas flotando sin cerrar los ojos.")

    def interaccionSocial(self):
        print("Nada en grupos llamados bancos entre peces")

    def imprimir(self):
        super().imprimir()

class Escarabajo(Animal):
    def moverse(self):
        print("Camina y puede volar distancias cortas")

    def comunicacion(self):
        print("Usa vibraciones o feromonas para comunicarse")

    def alimentarse(self):
        print("Se alimenta de hojas o madera")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie, pone huevos en el suelo")

    def adaptacion(self):
        print("Se adapta a cualquier entorno")

    def instintos(self):
        print("Busca alimento y pareja por instinto, solo busca sobrevivir")

    def descanso(self):
        print("Descansa escondido bajo hojas o piedras")

    def sueño(self):
        print("Se queda inmovil para descansar, es lo mas cercano a dormir para ellos")

    def interaccionSocial(self):
        print("Es mayormente solitario, excepto en reproducción")

    def imprimir(self):
        super().imprimir()

class Pato(Animal):
    def moverse(self):
        print("Camina, nada y puede volar")

    def comunicacion(self):
        print("Se comunica con graznidos o sonidos")

    def alimentarse(self):
        print("Se alimenta de plantas acuaticas, insectos pequeños y semillas")

    def reproduccion(self):
        print("Se reproduce de forma sexual entre su especie, pone huevos la hembra en un nido")

    def adaptacion(self):
        print("Tiene plumas impermeables para flotar y mantenerse seco, pueden adaptarse a diferentes climas")

    def instintos(self):
        print("Busca alimento y protege a sus crias por instinto")

    def descanso(self):
        print("Descansa en tierra o sobre el agua")

    def sueño(self):
        print("Duerme 10 horas al dia y suele dormir con un ojo abierto para vigilar su entorno")

    def interaccionSocial(self):
        print("Vive y migra en grupos")

    def imprimir(self):
        super().imprimir()


#Codigo principal
print("CABALLO")
ObjCaballo = Caballo("Caballo", "14 años", "heno", "llanura", "Medio", "Blanco")
ObjCaballo.imprimir()
ObjCaballo.moverse()
ObjCaballo.comunicacion()
ObjCaballo.alimentarse()
ObjCaballo.reproduccion()
ObjCaballo.adaptacion()
ObjCaballo.instintos()
ObjCaballo.descanso()
ObjCaballo.sueño()
ObjCaballo.interaccionSocial()

print("\nCOCODRILO")
ObjCocodrilo = Cocodrilo("Cocodrilo", "30 años", "carne", "llanura", "Pequeño", "verde")
ObjCocodrilo.imprimir()
ObjCocodrilo.moverse()
ObjCocodrilo.comunicacion()
ObjCocodrilo.alimentarse()
ObjCocodrilo.reproduccion()
ObjCocodrilo.adaptacion()
ObjCocodrilo.instintos()
ObjCocodrilo.descanso()
ObjCocodrilo.sueño()
ObjCocodrilo.interaccionSocial()

print("\nPEZ")
ObjPez = Pez("Pez", "2 años", "plancton", "rio", "Pequeño", "naranja")
ObjPez.imprimir()
ObjPez.moverse()
ObjPez.comunicacion()
ObjPez.alimentarse()
ObjPez.reproduccion()
ObjPez.adaptacion()
ObjPez.instintos()
ObjPez.descanso()
ObjPez.sueño()
ObjPez.interaccionSocial()

print("\nESCARABAJO")
ObjEscarabajo = Escarabajo("Escarabajo", "6 años", "hojas", "montaña", "Pequeño", "rojo")
ObjEscarabajo.imprimir()
ObjEscarabajo.moverse()
ObjEscarabajo.comunicacion()
ObjEscarabajo.alimentarse()
ObjEscarabajo.reproduccion()
ObjEscarabajo.adaptacion()
ObjEscarabajo.instintos()
ObjEscarabajo.descanso()
ObjEscarabajo.sueño()
ObjEscarabajo.interaccionSocial()

print("\nPATO")
ObjPato = Pato("Pato", "5 años", "plantas", "montaña", "Pequeño", "rojo")
ObjPato.imprimir()
ObjPato.moverse()
ObjPato.comunicacion()
ObjPato.alimentarse()
ObjPato.reproduccion()
ObjPato.adaptacion()
ObjPato.instintos()
ObjPato.descanso()
ObjPato.sueño()
ObjPato.interaccionSocial()


    