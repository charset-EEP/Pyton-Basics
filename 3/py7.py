#Faça um programa que leia 5 números e informe o maior número. 

num1=int(input(print("1°")))
num2=int(input(print("2°")))
num3=int(input(print("3°")))
num4=int(input(print("4°")))
num5=int(input(print("5°")))
num=[num1,num2,num3,num4,num5]
num.sort()
print(num[4])
