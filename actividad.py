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
