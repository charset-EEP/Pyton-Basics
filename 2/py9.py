#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1=int(input(print("Digite o primeiro numero")))
num2=int(input(print("Digite o segundo numero")))
num3=int(input(print("Digite o terceiro numero")))
num=[num1,num2,num3]
num.sort(reverse=True)
print (num)

