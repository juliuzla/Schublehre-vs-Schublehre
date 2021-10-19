import pandas as pd
import math
import scipy.integrate
import scipy.stats

Data = pd.read_table(r'Schublehre vs Schublehre.txt')

#Daten als Array

RoterSteinAnalog = Data['Roter Stein, analoge Schublehre']

RoterSteinDigital = Data['Roter Stein, digitale Schublehre']

GelberSteinAnalog = Data['Gelber Stein, analoge Schublehre']

GelberSteinDigital = Data['Gelber Stein, digitale Schublehre']

def mean(values): #Funktion zur Berechnung des Mittelwerts
    
    return sum(values)/len(values)

def stanDev(values): #Funktion zur Berechnung der Standartabweichung

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

print(scipy.stats.ttest_ind_from_stats(
    mean(RoterSteinDigital), stanDev(RoterSteinDigital),len(RoterSteinDigital)
    ,mean(RoterSteinAnalog), stanDev(RoterSteinAnalog),len(RoterSteinAnalog)
    ,alternative='two-sided'
)) #berechnet P-Wert und gibt ihn aus

print(T_Wert(GelberSteinDigital, GelberSteinAnalog))

print(scipy.stats.ttest_ind_from_stats(
    mean(GelberSteinDigital), stanDev(GelberSteinDigital),len(GelberSteinDigital)
    ,mean(GelberSteinAnalog), stanDev(GelberSteinAnalog),len(GelberSteinAnalog)
    ,alternative='two-sided'
)) #berechnet P-Wert und gibt ihn aus