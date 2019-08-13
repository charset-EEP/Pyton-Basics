#Faça um programa que peça as 4 notas bimestrais e mostre a média.

nota=0
j=1

for i in range(4): 
    x=(input(print("Digite a nota da "+str(j)+"° prova bimestral")))
    nota=nota+int(x)
    j=j+1
nota=nota/4

print("Média: "+str(nota))
