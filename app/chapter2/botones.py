#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import Tkinter
from Tkinter import *
import tkMessageBox


def view_botones():
  top = Tkinter.Tk()
  btn = Tkinter.Button(top, text ="Python for Beginners", command = helloCallBack)
  btn.pack()
  top.mainloop()

  

def helloCallBack():
   tkMessageBox.showinfo( "Python for Beginners", "Hola, mundo")

