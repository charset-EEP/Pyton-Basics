#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

preço1=int(input(print("Digite o primeiro preço")))
preço2=int(input(print("Digite o segundo preço")))
preço3=int(input(print("Digite o terceiro preço")))
num=[preço1,preço2,preço3]
num.sort(reverse=True)
print (str(num[2])+" é o mais barato")

