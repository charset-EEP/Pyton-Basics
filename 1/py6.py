#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio=float(input(print("Digite o raio do circulo")))
raio=round(math.pi*raio*raio,2)
print("Área: "+str(raio))
