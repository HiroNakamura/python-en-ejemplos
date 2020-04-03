#!/bin/python
# coding=utf-8


def menu():
    opcion = int(str('2'))
    if opcion == 1:
        print("Elegiste la opción 1")
    elif opcion == 2:
        print("Elegiste la opción 2")
    else:
        print("Tu opcion es: ",opcion)
        
        
def get_color_rojo(color):
    color = "Rojo" if color == 'red' or color == 'Red' else "Tu color es "+color
    return color
