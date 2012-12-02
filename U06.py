#!/usr/bin/python
# encoding=utf-8

"""Übung 06 Pendel"""
#Markus Klemm WS12/13 Phy-BA

import numpy as np
import math
import matplotlib.pyplot as plt

#ToDo ArgParse

FILENAME = "Pendel-Messung.dat"

f = np.loadtxt(FILENAME)

#Aufgabe 1
print "Mittelwert: " + str(np.mean(f))
print "Varianz: " + str(np.var(f)) + "s"
print "Standardabweichug des Mittelwerts: " + str(float(np.std(f,ddof=1)/math.sqrt(len(f)))) + "s"

#Aufgabe 2

def myStat(myarray):
    """Gibt den Mittelwert, die Varianz und die Standardabweichung zum Mittelwert, des übergebenen np.arrays, zurück"""
    quer = str(np.mean(myarray))
    var = str(np.var(myarray)) + "s"
    sigmamittelwert = str(float(np.std(myarray,ddof=1)/math.sqrt(len(myarray)))) + "s"
    return (quer,var,sigmamittelwert)
 


for x in range(len(f)+1):
    tmp = f[:x+1]
    myStat(tmp)

#Aufgabe 3
plt.figure()
plt.ylabel("Zeit in s")
plt.xlabel("Messung")
plt.title("Entwicklung von Mittelwert und stat. Messabweichung")
plt.plot(f,'go', label='Messwerte')

#Errorbars für Messwerte
for x in range(len(f)):
    x_z = np.std(f,ddof=1)/math.sqrt(len(f)) #Berechnung zufällige Messabweichung
    plt.errorbar(x,f[x],x_z)

#Entwicklung Mittelwert
plt.subplot()


plt.figure()
plt.hist(f)
plt.show()

