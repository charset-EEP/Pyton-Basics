#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor=[]
for i in range(10):
    vetor.append(int(input()))
    vetor[i]=vetor[i]*vetor[i]
print(sum(vetor))
