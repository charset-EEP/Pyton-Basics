#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

vetor=[]
mul=1
for i in range(5):
    vetor.append(int(input()))
print(sum(vetor))
for i in range(5):
    mul=vetor[i]*mul
print(mul)
