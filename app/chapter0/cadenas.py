#!/bin/python
# coding=utf-8

CADENA_GLOBAL = "Python for Beginners"

def cadenas():
  global CADENA_GLOBAL
  print CADENA_GLOBAL
  print "Tamaño: ",len(CADENA_GLOBAL)
  print "Minusculas: ",CADENA_GLOBAL.lower()
