#!/bin/python
# coding=utf-8

import datetime
import calendar


def get_dia_de_semana(dia):
    dia_semana =''
    if dia == calendar.MONDAY:
        dia_semana = 'Fue un Lunes'
    if dia == calendar.TUESDAY:
        dia_semana = 'Fue un Martes'
    if dia == calendar.WEDNESDAY:
        dia_semana = 'Fue un Miercoles'
    if dia == calendar.THURSDAY:
        dia_semana = 'Fue un Jueves'
    if dia == calendar.FRIDAY:
        dia_semana = 'Fue un Viernes'
    if dia == calendar.SATURDAY:
        dia_semana = 'Fue un Sabado'
    if dia == calendar.SUNDAY:
        dia_semana = 'Fue un Domingo'
    else:
        dia_semana = 'fue un dia de Verano'

    return dia_semana



def testA():
    print("\tDatetime")
    print("Maximo: ",datetime.MAXYEAR)
    print("Minimo: ",datetime.MINYEAR)
    hoy = datetime.date.today()
    print("Hoy es: ",hoy)
    antes = datetime.date(2019, 12, 18)
    print("Fecha de antes: ",antes)
    antes = datetime.date(2020,2,12)
    print("Fecha de antes: ",antes)
    today = datetime.today() 
    print("Año:", today.year)
    print("Mes:", today.month)
    print("Dia:", today.day)


def testB():
    print("\tCalendar")
    print(calendar.weekheader(3))
    print(calendar.firstweekday())
    print(calendar.month(2018,4))
    print(calendar.calendar(2010))
    print(calendar.calendar(2011))
    print("Lunes vale: ",calendar.MONDAY)
    print("Martes vale: ",calendar.TUESDAY)
    print("Miercoles vale: ",calendar.WEDNESDAY)
    print("Jueves vale: ",calendar.THURSDAY)
    print("Viernes vale: ",calendar.FRIDAY)
    print("Sabado vale: ",calendar.SATURDAY)
    print("Domingo vale: ",calendar.SUNDAY)
    dia_de_la_semana = calendar.weekday(2011,12,18)
    print("Dia de la semana: ",dia_de_la_semana)
    print("Dia de la semana: ",get_dia_de_semana(dia_de_la_semana))
    is_leap = calendar.isleap(2011)
    bisiesto = "Fue año bisiesto" if is_leap == True else "No fue año bisiesto"
    print(bisiesto)



def main():
    testA()
    testB()


if __name__ == '__main__':
    main()