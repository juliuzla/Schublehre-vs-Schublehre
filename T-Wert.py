import pandas as pd
import math
import scipy.integrate
import scipy.stats

Data = pd.read_table(r'Schublehre vs Schublehre.txt')

#Daten als Array

RoterSteinAnalog = Data['Roter Stein, analoge Schublehre']

RoterSteinDigital = Data['Roter Stein, digitale Schublehre']

def mean(values): #Funktion zur Berechnung des Mittelwerts
    
    return sum(values)/len(values)

def stanDev(values): #Funktion zur Berechnung der StandartabweichungA

    n = len(values)

    x = 0
    
    for i in range(len(values)):

        x += (values[i]-mean(values))**2

    return math.sqrt(x/n)

def T_Wert(values1, values2): #Funktion zur Berechnung des T-Werts

    n = len(values1) #für gleich lange Listen

    return math.sqrt(n/((stanDev(values1))**2+(stanDev(values2))**2))*(mean(values1)-mean(values2))

#Signifikantsniveau = 0.05

print(T_Wert(RoterSteinDigital, RoterSteinAnalog)) #gibt T-Wert aus

print(scipy.stats.ttest_rel(RoterSteinDigital, RoterSteinAnalog)) #berechnet P-Wert und gibt ihn aus
