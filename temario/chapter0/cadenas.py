#!/bin/python
# -*- coding: utf-8 -*-

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
  print("Mayusculas: ",CADENA_GLOBAL.upper())
  print("Primer caracter",CADENA_GLOBAL[0])
  cadena = CADENA_GLOBAL
  verdadero = "Es digito" if cadena.isdigit() else "No es digito"
  print(verdadero)
  print("Tipo: ",type(cadena))
  vector = cadena.split(" ")
  print("Vector: ",vector)#["Python","for","Beginners"]
  nombre = "Norma"
  print(f"Cadena: {nombre.capitalize()}")
  print(f"Primera letra de {nombre}: {nombre[0]}")
  longitud = len(nombre)
  print(f"Útlima letra de {nombre.capitalize()}: {nombre[longitud-1]}  ")
  lista = [None, 121, 'R',True, 43,None, False, "5"]
  numeros = list()
  for n in lista:
    print("Tipo: ",type(n))
    if str(type(n)) == "<class 'str'>":
      print("Cadena: ",n)
      if n.isdigit():
        print("Numero: ",n)
        numeros.append(n)

  print("Hay ",len(numeros)," numero(s) en la lista")
  print("Numero: ",numeros)
  archivos = ["doc.xml","doc.pdf","archivo.xml","datos.csv"]
  for arch in archivos:
    if arch.endswith(".xml"):
      print(arch)
  
  
  
def cadenas_strings():
  global CADENA_GLOBAL
  nombre = CADENA_GLOBAL
  print("Longitud: ",len(nombre))
  print(nombre.upper())
  print(nombre[0:6]) #Python
  print(nombre[0]) #P
  print(nombre[6:10]) #for
  print("Recorriendo caracteres de cadena:")
  for i in nombre:
    print(i)



def main():
  cadenas()
  #cadenas_strings()


if __name__ == '__main__':
    main()



