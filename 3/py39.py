#Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

alto=0
baixo=10000
for i in range(10):
    naluno=int(input())
    alt=float(input())
    if alt>alto:
        alto=alt
    if alt<baixo:
        baixo=alt
print(alto)
print(baixo)
