#Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

from random import randint
import collections
dado=[]
for i in range(100):
    dado.append(randint(1,6))
c=collections.Counter(dado)
print(c)

