#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Enumeraciones en Python
'''


import enum

class Programador(enum.Enum):
   Junior = 1
   Mid_Level = 2
   Senior = 3


class PuntosCardinales:
      NORTE = 0
      SUR = 1
      ESTE = 2
      OESTE = 3
     
     
class TAMANYO:
      CHICO = 10.0
      MEDIANO = 15.0
      GRANDE = 22.0



class LENGUAJES:
      PYTHON = "Python"
      JAVA = "Java"
      GOLANG = "Golang"
      KOTLIN = "Kotlin"
      GROOVY = "Groovy"
      CSHARP = "C#"
      JAVASCRIPT = "Javascript" 
      
def main():
      print(LENGUAJES.PYTHON)
      print(TAMANYO.GRANDE)
      print(PuntosCardinales.NORTE)
      print("Valor: ",end="")
      print("Nombre: ",end="")
      print(Programador.Senior)
      print("Repr : ",end="")
      print(repr(Programador.Senior))
      print("Type : ",end ="")
      print(type(Programador.Senior))
      print(Programador.Senior)
      junior = Programador.Junior
      print(junior)
      print(junior.name)
      print("\tRecorriendo enumeracion:")
      for progr in (Programador):
            print(progr,": ",progr.name)



if __name__ == '__main__':
    main()     
