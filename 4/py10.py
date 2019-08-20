#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

vet1=[]
vet2=[]
vet3=[]
for i in range(10):
    vet1.append(input())
    vet3.append(vet1[i])
    vet2.append(input())
    vet3.append(vet2[i])
print(vet1)
print(vet2)
print(vet3)

    
