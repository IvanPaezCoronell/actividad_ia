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

# 8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.
horas = float(input('Digite las horas trabajadas: '))
pagoHoras = horas * 20000
cajaAhorro = pagoHoras * 0.05
descuento = pagoHoras - cajaAhorro
print('Descuento  por concepto de caja de ahorros: ', cajaAhorro)
print(f'Valor total a pagar al profesor: ${descuento}')

# 9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.
montoInicial = float(input('Digite el valor de la tarjeta inicial: '))
montoFinal = float(input('Digite el valor de la tarjeta final: '))
costoLlamada = (montoInicial - montoFinal) / 0.2
print('El costo de la llamada es de $', costoLlamada)

# 10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un algoritmo que determine el monto a pagar por un
# revelado completo sabiendo que adiconalmente le cobran el IVA
# (16%).
nFotos = float(input('Digite el numero de fotos a revelar: '))
revelado = nFotos * 15000
costoFinal = (revelado * 0.16) + revelado
print('El costo total del revealdo con iva es de $', costoFinal)

# 11. En un hospital existen tres áreas: Ginecología 40%, Pediatría 30% y
# Traumatología 30%. Obtener la cantidad de dinero que recibirá cada área,
# para cualquier monto presupuestal.
montoPresupuestal = float(input('Digite el monto presupuestal: $'))
g = montoPresupuestal * 0.40
t = montoPresupuestal * 0.30
p = montoPresupuestal * 0.30
print(f'Ginecologia ${g}', f'\nTraumatologia ${t}', f'\nPediatria ${p}')

# 12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# algoritmo que teniendo como dato de entrada el total de películas
# alquiladas, y el número de días de alquiler, determine el monto a
# pagar.
nPeliculas = float(input('Digite el numero de peliculas alquiladas: '))
dias = float(input('Digite el dumero de dias a alquilar: '))
total = (nPeliculas * dias * 15000)
print('El valor total a pagar es de: $', total)

# 13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un algoritmo que determine el monto a
# pagar por una familia que desee realizar dicho Tour sabiendo que
# también cobran el 12% de IVA.
nPersonas = float(input('Digite el numero de personas: '))
monto = nPersonas * 25000
iva = (monto * 0.12) + monto
print('el total a pagar es: ', iva)

# 14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un algoritmo que determine el valor
# total a pagar por la habitación si la estadía fue de varios días.
day = int(input('Digite el numero de dias a hospedar: '))
if day == 1:
    print('Debe pagar $100000')
else:
    total = (day * 200000) - 100000
    print('Debe pagar: $', total)
