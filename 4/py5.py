#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par=[]
impar=[]

for i in range(20):
    num=int(input())
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
print(par)
print(impar)
