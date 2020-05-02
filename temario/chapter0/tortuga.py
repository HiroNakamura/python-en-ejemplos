#!/bin/python
# coding=utf-8

#from turtle import *
import turtle

def testA():
  wn = turtle.Screen()
  wn.bgcolor("light gray")
  wn.title("Comenzando con Tortuga")
  skk = turtle.Turtle()
  skk.forward(100)
  turtle.done()

def testB():
  skk = turtle.Turtle() 
  for i in range(4): 
    skk.forward(50) 
    skk.right(90)
  turtle.done() 


def testC():
  star = turtle.Turtle() 
  for i in range(50): 
    star.forward(50) 
    star.right(144)  
  turtle.done()


def testD():
  polygon = turtle.Turtle()
  num_sides = 6
  side_length = 70
  angle = 360.0 / num_sides  
  for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
  turtle.done() 



def main():
  #testA()
  #testB()
  #testC()
  testD()

if __name__ == '__main__':
    main()
