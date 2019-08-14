#Faça um Programa que leia três números e mostre o maior e o menor deles. 

num1=int(input(print("Digite o primeiro numero")))
num2=int(input(print("Digite o segundo numero")))
num3=int(input(print("Digite o terceiro numero")))
num=[num1,num2,num3]
num.sort()
print (str(num[2])+" é o maior")
num.sort(reverse=True)
print (str(num[2])+" é o menor")
