#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Enumeraciones en Python
'''

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


if __name__ == '__main__':
    main()     
