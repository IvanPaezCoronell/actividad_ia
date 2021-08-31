#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:10:54 2021

@author: ivandavid
"""

# 1. Haga un algoritmo que calcule la masa de la siguiente fórmula:
# Masa = (presión * volúmen) / (0.37 * (temperatura + 460))
presion = float(input('Digite el valor de la presion: '))
volumen = float(input('Digite el valor del volumen: '))
temperatura = float(input('Digite el valor de  la temperatura: '))
masa = (presion * volumen) / (0.37 * (temperatura + 460))
print('La masa es: ', masa)

# 2. Calcular el número de pulsaciones que una persona debe tener por
# cada 10 segundos de ejercicio, si la fórmula es:
# Num. Pulsaciones = (200 – edad) /10.
edad = input('Digite su edad: ')
numPulsaciones = (200 - int(edad))/10
print('El numero de pulsaciones que debe tener es de: ', numPulsaciones)

# 3. Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.'''
p1 = float(input('Digite el valor que va a invertir la 1ra persona: $'))
p2 = float(input('Digite el valor que va a invertir la 2da persona: $'))
p3 = float(input('Digite el valor que va a invertir la 3ra persona: $'))
inversionTotal = p1 + p2 + p3
porcentajep1 = (p1 / inversionTotal) * 100
porcentajep2 = (p2 / inversionTotal) * 100
porcentajep3 = (p3 / inversionTotal) * 100
print('La inversion total es de $', inversionTotal)
print(f'El porcentaje de la 1ra es de {porcentajep1}%')
print(f'El porcentaje de la 2da es de {porcentajep2}%')
print(f'El porcentaje de la 3ra es de {porcentajep3}%')

# 4. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.
saldoInicial = float(input('Digite el saldo inicial: $ '))
saldoFinal = (saldoInicial * 0.015) + saldoInicial
print('El saldo final es de: $', saldoFinal)
