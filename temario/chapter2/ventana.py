#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

#Ventana
def get_ventana():
    ventana = Tk()
    ventana.title("Python for Beginners")
    ventana.geometry("1000x300+0+0")
    ventana.resizable()
    Tops = Frame(ventana,bg="steelblue",width = 1600,height=50,relief=SUNKEN)
    Tops.pack(side=TOP)
    ventana.mainloop()


def main():
	get_ventana()


if __name__ == '__main__':
    main()