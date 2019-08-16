#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1=int(input(print("Digite o primeiro numero")))
num2=int(input(print("Digite o segundo numero")))
for i in list(range(num1,num2)):
    print(i)
