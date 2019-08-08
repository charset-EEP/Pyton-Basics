#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

x=float(input(print("Digite o raio do circulo")))
x=round(math.pi*x*x,2)
print("Área: "+str(x))
