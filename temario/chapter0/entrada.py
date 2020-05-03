#!/bin/python
# -*- coding: utf-8 -*-


def introduce_cadena():
    cadena = input("Introduce cadena:")
    print("Cadena: ",cadena)


def introduce_numero():
    numero = input("Introduce numero:")
    if numero.isdigit():
        numero = int(numero)
        print("Numero: ",numero)
    else:
        print("Parece que no es un numero: ",numero)


def main():
    introduce_cadena()
    introduce_numero()


if __name__ == '__main__':
    main()