#!/usr/bin/env python
# -*- coding: utf-8 -*-


import mysql.connector

def conectando(my_host, usuario, passw):
    print("Conectando...")
    mydb = mysql.connector.connect(host=my_host,user=usuario,password=passw)
    resultado = False
    if mydb != None:
        resultado = True
    return resultado


def operaciones():
    mydb = mysql.connector.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE python_db")
    print("Base de datos creada")
    mycursor.execute("DROP DATABASE python_db")
    print("Base de datos eliminada")
    mycursor.execute("SHOW DATABASES")
    print("Listamos las bases de datos:")
    for x in mycursor:
        print(x)
    mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="curso_udemy")
    if mydb!=None:
        print("Te has conectado a la BD 'curso_udemy'")
        mycursor = mydb.cursor()
        mycursor.execute("CREATE TABLE tecnicos(id int auto_increment primary key,nombre VARCHAR(255), departamento VARCHAR(255))")
        print("Se creo la tabla 'tecnicos'")
        mycursor.execute("SHOW TABLES")
        print("Listamos las tablas:")
        for x in mycursor:
            print(x)
        sql = "INSERT INTO tecnicos (nombre, departamento) VALUES (%s, %s)"
        val = ("Julia torres", "Finanzas")
        mycursor.execute(sql, val)
        mydb.commit()
        print("Se ha registrado, ID:", mycursor.lastrowid)
        mycursor.execute("drop table tecnicos")
        print("Tabla 'tecnicos' borrada")


def conectando():
    if conectando("localhost","root","root"):
        print("Conexion exitosa!")
    else:
        print("Conexion fallida!")


def main():
    conectando()
    operaciones()


if __name__ == '__main__':
    main()