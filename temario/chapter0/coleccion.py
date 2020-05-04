#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Uso de Set
def coleccion():
    set_1 = set()
    print(set_1)
    set_2 = set([1,2,3,4,5])
    print(set_2)
    set_3 = {1,2,3,4,}
    print(set_3)
    causa = ''
    try:
        set_4 = set_1 + set_2
        print(set_4)
    except TypeError as error:
        print("Ha ocurrido una excepcion: operacion invalida")
        causa = 'La causa ha sido: '+str(error)
    finally:
        print(causa)
    print("************************************************")
    cadena = set('El extraño caso de la serpiente programadora.')
    print("Contenido:\n",cadena)
    for c in cadena:
        print(c)

    
    
    
def main():
	coleccion()


if __name__ == '__main__':
    main()
