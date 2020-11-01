#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import platform
import sys

def limpiar():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def info_system():
    print('Sistema: ',platform.system())
    print('Plataforma: ',platform.release())
    print('Version: ',platform.version())
    print(sys.version.split('\n'))
    print('Procesador: ',platform.machine())
    print('Plataforma: ',platform.platform())
    print('Nombre: ',platform.uname())
    print(platform.mac_ver())


def main():
    limpiar()
    info_system()


if __name__ == '__main__':
    main()