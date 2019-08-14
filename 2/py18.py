#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data=input(print("Digite a data"))
invalido=0

if len(data)>10:
    invalido+=1
if int(data[1])>3:
    invalido+=1
if int(data[3])!=1:
    invalido+=1
if invalido>0:
    print("Data inválida")
else:
    print("Data Valida")
    print(data)

