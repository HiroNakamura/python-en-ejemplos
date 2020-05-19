#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from re import search


#funciones de cadena
def testA():
    print("Funciones de cadena:")
    cadena = 'Python'
    print("Cadena: ",cadena)
    print("Longitud de cadena: ",len(cadena))
    for cad in cadena:
        print(cad)
    existe = "Existe 'y' en la cadena" if "y" in cadena else "No existe 'y' en la cadena"
    print(existe)
    print("'Python'.find('P'): ", cadena.find('P'))
    print("'Python'.find('h'): ", cadena.find('h'))
    try:
        print("'Python'.find('W'): ", cadena.find('W'))
    except ValueError as error:
        print("Ha ocurrido un error: ",str(error))
    finally:
        print("")
    print("'Python'.index('P'): ", cadena.index('P'))
    print("'Python'.index('h'): ", cadena.index('h'))
    try:
        print("'Python'.index('W'): ", cadena.index('W'))
    except ValueError as error:
        print("Ha ocurrido un error: ",str(error))
    finally:
        print("")
    print("MAYUSCULA".lower())
    print("minuscula".upper())
    lista = ["doc.pdf","1233.pdf","datos.xml","documentos.pdf"]
    xml = "Es un documento XML" if lista[2].endswith(".xml") == True else "No es un documento XML"
    print(xml)
    if lista[0].startswith("doc") == True:
        print(lista[0])
    print("'Python'[0:3] : ",cadena[0:3])
    print("'FERROCARRILERO'[3:5] : ",'FERROCARRILERO'[3:7])

#Regex
def testB():
    cadena = "123"
    print("Cadena: ",cadena)
    print(re.search('123', cadena))
    if re.search('123', cadena):
        print("Patron encontrado")
    else:
        print("No se ha encontrado el patron")
    if re.search('ABC', cadena):
        print("Patron encontrado")
    else:
        print("No se ha encontrado el patron")
    print("***********************************************")
    cadena = "El retrato de una odisea sin nombre."
    patrones = ["retrato","odisea"]
    for patron in patrones:
        print('%s in %s'%(patron, cadena),end='')
        if re.search(patron, cadena):
            print(">>Patron encontrado: ",patron)
        else:
            print(">>Patron no encontrado")
    cadena = "La programacion es divertida."
    print("Cadena: ",cadena)
    encontrado = re.findall(r"^\w+",cadena)
    print("Encontrado: ",encontrado)


def main():
    testA()
    testB()
    
if __name__ == '__main__':
   main()
