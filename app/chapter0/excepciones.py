#!/bin/python
# coding=utf-8


def excepcion_testA():
    try:
       import noExiste()
    except e:
       print "Ha ocurrido una excepcion: ",e
