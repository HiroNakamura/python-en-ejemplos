#!/bin/python
# coding=utf-8

MAX = 100

def ciclo_for():
    global MAX
    print "Ciclo for:"
    for i in range(1,MAX):
    	if i%3 == 0 and i%5 ==0:
    		print "No. ",i
