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
    quer = np.mean(myarray)
    var = np.var(myarray)
    sigmamittelwert = float(np.std(myarray,ddof=1)/math.sqrt(len(myarray)))
    return (quer,var,sigmamittelwert)
 


for x in range(len(f)+1):
    tmp = f[:x+1]
    myStat(tmp)

#Aufgabe 3
plt.subplot(221)
plt.ylabel("Zeit in s")
plt.xlabel("Messung")
plt.plot(f, label='Messwerte')
plt.title("Messwerte")
#Errorbars für Messwerte
for x in range(len(f)):
    x_z = np.std(f,ddof=1)/math.sqrt(len(f)) #Berechnung zufällige Messabweichung
    plt.errorbar(x,f[x],x_z)


plt.subplot(222)
plt.title("Mittelwert")
xquer = np.empty(0)
#Entwicklung Mittelwert
for x in range(len(f)+1):
    tmp = f[:x+1]
    
    global xquer
    xquer = np.append(xquer,myStat(tmp)[0])
    plt.errorbar(x,xquer[x],myStat(tmp)[2],ecolor='b')

plt.plot(xquer,label="Mittelwerte")

plt.show()

