#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    #o produto do dobro do primeiro com metade do segundo .
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo. 

n1=int(input(print("Digite o 1° numero")))
n2=int(input(print("Digite o 2° numero")))
n3=float(input(print("Digite o 3° numero")))

a=(2*n1)*(n2/2)
b=(3*n1)+n3
c=n3*n3*n3

print("A) "+str(a))
print("B) "+str(b))
print("C) "+str(c))
