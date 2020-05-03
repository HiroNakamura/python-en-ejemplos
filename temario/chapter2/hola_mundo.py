#!/usr/bin/env python
# -*- coding: utf-8 -*-


from tkinter import *


class Application(Frame):
    def say_hi(self):
        print("Hola, mundo en Tkinter")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUITAR"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hola",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
root.title("Python for Beginners")
root.geometry("1000x300+0+0")
Tops = Frame(root,bg="steelblue",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)
app.mainloop()
root.destroy()