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
print "Standardabweichung: " + str(numpy.std(f))
print "Varianz: " + str(numpy.var(f))
print "Standardabweichug des Mittelwerts: " + str(float(numpy.std(f)/math.sqrt(numpy.size(f))))


