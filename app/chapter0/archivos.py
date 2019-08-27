#!/bin/python
# coding=utf-8


ARCHIVO = "datos.csv"

def leer_archivo():
  global ARCHIVO
  if open(ARCHIVO,"r"):
    print "Parece que el archivo existe"
  file = open(ARCHIVO,"r")
  print type(file)
  print "Contenido:",file.readlines()


