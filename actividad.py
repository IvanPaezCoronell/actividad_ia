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

# 5. Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# algoritmo que determine el monto de cada descuento y el monto total
# a pagar al trabajador.
sueldoBase = float(input('Digite el sueldo base del trabajador: $'))
pp = sueldoBase * 0.01
ss = sueldoBase * 0.04
sf = sueldoBase * 0.0005
ca = sueldoBase * 0.05
saldoTotal = (sueldoBase - pp - ss - sf - ca)
print('El descuento por ley de politica publica es de: $', pp)
print('El descuento por seguro social es de: $', ss)
print('El descuento por seguro forzoso es de: $', sf)
print('El descuento por caja de ahorro es de: $', ca)
print('El saldo total a pagar es de $', saldoTotal)

# 6. El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.'''
palabras = float(input('Numeros de palabras a agregar: '))
centimetro = float(input('Digite el tamaño en centimetros del aviso: '))
colores = float(input('Cantidad de colores: '))
total = (palabras * 20000)+(centimetro * 15000)+(colores * 25000)
print(f'El costo total del aviso es de ${total}')

# 7. Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un algoritmo que determine el monto del bono
# a pagar a un trabajador que tiene varios años en la empresa.
añosTrabajando = float(input('Digite los años que lleva trabajando: '))
bono = (añosTrabajando * 120000) + 100000
print(f'El bono a pagar es de: ${bono}')
