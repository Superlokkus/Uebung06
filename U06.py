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
x_z = []
for x in range(len(f)):
    global x_z
    x_z.append(np.std(f,ddof=1)/math.sqrt(len(f))) #Berechnung zufällige Messabweichung
    #plt.errorbar(x,f[x],x_z)

plt.errorbar(range(len(f)),f,x_z, label="Zufaellige Messabweichung")
plt.legend(fontsize="xx-small")
plt.subplot(222)
plt.ylabel("Zeit in s")
plt.xlabel("Messung")
plt.title("Entwicklung des Mittelwertes")
#Entwicklung Mittelwert
xquer = np.empty(0)
stdxquer = np.empty(0)
for x in range(len(f)+1):
    tmp = f[:x+1]
    
    global xquer
    global stdxquer
    xquer = np.append(xquer,myStat(tmp)[0])
    stdxquer = np.append(stdxquer,myStat(tmp)[2])
    
plt.errorbar(range(len(f)+1),xquer,stdxquer, label="Std. Abweichung Mittelwert")

plt.plot(xquer,label="Mittelwerte")
plt.legend(fontsize="xx-small")

#Aufgabe 4
plt.subplot(223)
plt.hist(f,int(math.sqrt(len(f))))
plt.subplot(224)
plt.hist(f,int(math.sqrt(len(f))),normed=True)

plt.show()

