#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

n1=int(input())
n2=n1+1
for i in range(n2):
    primo=1
    for j in range(i):
        if j>1:
            if i%j==0:
                primo=0
    if primo==1:
        print(i)
