from Botellas import Botella
from BotellaVidrio import BotellaVidrio
from BotellaPlastico import BotellaPlastico

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