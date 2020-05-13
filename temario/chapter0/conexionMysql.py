#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mysql.connector as mariadb


def conecta():
    """ Conectandonos a la abse de datos MySQL"""
    hecho = 'Hecho, hemos terminado. Conexion cerrada.'
    consultora_ = 'Jade'
    try:
        mariadb_connection = mariadb.connect(user='root', password='root', database='curso_udemy')
        cursor = mariadb_connection.cursor()
        print("Se ha conectado a la base de datos Mysql")
        cursor.execute("SELECT nombre, email, consultora FROM empleados WHERE consultora=%s", (consultora_,))
        try:
            for nombre, email, consultora  in cursor:
                print(nombre,", ",email,", ",consultora)
        except AttributeError as errorA:
            print('Ha ocurrido un error de atributo')
            hecho = 'Error: '+str(errorA)
        mariadb_connection.close()
    except ConnectionError as error:
        print("Ha ocurrido un error al tratar de conectarse")
        hecho = 'Error: '+str(error)
    finally:
        print(hecho)



def main():
    conecta()


if __name__ == '__main__':
    main()