#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import Tkinter
from tkinter import *
import tkMessageBox


def view_botones():
  top = Tk()
  btn = Button(top, text ="Python for Beginners", command = helloCallBack)
  btn.pack()
  top.mainloop()

  

def helloCallBack():
   tkMessageBox.showinfo( "Python for Beginners", "Hola, mundo")



def main():
	pass


if __name__ == '__main__':
    main()