#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. 

x=[]
par=0
impar=0
for i in range(10):
    x.append(int(input(print("num"))))
    if x[i] % 2 == 0:
        par+=1
    else:
        impar+=1
print(par)
print(impar)
    
