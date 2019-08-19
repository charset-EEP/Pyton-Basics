#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem. 

num=int(input(print("Numero: ")))
ex=int(input(print("Expoente: ")))
numex=1
for i in range(ex):
    numex=numex*num
print(numex)
