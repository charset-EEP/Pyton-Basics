#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

CD=int(input(print("Quantos CD's?")))
custo=0
for i in range(CD):
    custo+=int(input(print("$")))
media=custo/CD
print(media)
