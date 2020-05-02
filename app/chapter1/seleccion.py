#!/bin/python
# coding=utf-8

from PyZenity import Question
from PyZenity import InfoMessage


#Question
def linux_instalado():
    if Question('Tienes instalado Linux?',width=250,height=140,title="Python for Beginners"): #nos devolverá un booleano
        InfoMessage('Bienvenido al udo Linuxero',width=250,height=140,title="Python for Beginners")
    else:
        InfoMessage('Deberias instalar Linux',width=250,height=140,title="Python for Beginners")


def main():
	pass


if __name__ == '__main__':
    main()