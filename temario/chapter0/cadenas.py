#!/bin/python
# coding=utf-8

'''
Autor: Fer Carraro
Fecha:  02/04/2020
'''

CADENA_GLOBAL = "Python for Beginners"


def cadenas():
  global CADENA_GLOBAL
  print(CADENA_GLOBAL)
  print("Tamaño: ",len(CADENA_GLOBAL))
  print("Minusculas: ",CADENA_GLOBAL.lower())
  
  
  
def cadenas_strings():
  nombre = "Python for beginners"
  print("Longitud: ",len(nombre))
  print(nombre.upper())
  print(nombre[0:6]) #Python
  print(nombre[0]) #P
  print(nombre[6:10]) #for
  for i in nombre:
    print(i)



def main():
  cadenas()
  cadenas_strings()


if __name__ == '__main__':
    main()



