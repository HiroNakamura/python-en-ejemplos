#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import Tkinter
from tkinter import *
import tkinter.messagebox


def view_botones():
  top = Tk()
  top.title("Python for Beginners")
  top.geometry("1000x300+0+0")
  top.resizable()
  Tops = Frame(top,bg="steelblue",width = 1600,height=50,relief=SUNKEN)
  Tops.pack(side=TOP)
  btn = Button(top, text ="Python for Beginners", command = helloCallBack)
  btn.pack()
  top.mainloop()

  
def helloCallBack():
  tkinter.messagebox.showinfo( "Python for Beginners", "Hola, mundo.\nPython for Beginners!!")


def main():
  view_botones()


if __name__ == '__main__':
    main()