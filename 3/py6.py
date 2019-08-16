#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

for i in range(21):
    print(i)

for j in range(20):
    jj=j
    j=j+1
    print(str(jj)+" "+str(j))
    
