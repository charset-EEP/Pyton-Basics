#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
y=0
z=1
for i in range(4): 
    x=(input(print("Digite a nota da "+str(z)+"° prova bimestral")))
    y=y+int(x)
    z=z+1
y=y/4
print("Média: "+str(y))
