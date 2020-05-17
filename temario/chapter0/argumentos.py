#!/bin/python
# coding=utf-8


import sys


def main():
    print("Nombre del script: ", sys.argv[0])
    print("Numero de argumentos: ", len(sys.argv))
    print("Los argumentos son: " , str(sys.argv))

if __name__ == '__name__':
    main()