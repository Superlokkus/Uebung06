#!/usr/bin/python
# encoding=utf-8

"""Übung 06 Pendel"""
#Markus Klemm WS12/13 Phy-BA

import numpy
import math

#ToDo ArgParse

FILENAME = "Pendel-Messung.dat"

f = numpy.loadtxt(FILENAME)

#Aufgabe 1
print "Mittelwert: " + str(numpy.mean(f))
print "Varianz: " + str(numpy.var(f)) + "s"
print "Standardabweichug des Mittelwerts: " + str(float(numpy.std(f,ddof=1)/math.sqrt(len(f)))) + "s"

#Aufgabe 2

def myStat(myarray):
    """Gibt den Mittelwert, die Varianz und die Standardabweichung zum Mittelwert, des übergebenen numpy.arrays, zurück"""
    quer = str(numpy.mean(myarray))
    var = str(numpy.var(myarray)) + "s"
    sigmamittelwert = str(float(numpy.std(myarray,ddof=1)/math.sqrt(len(myarray)))) + "s"
    return (quer,var,sigmamittelwert)
   
for x in range(len(f)+1):
    tmp = f[:x+1]
    myStat(tmp)


