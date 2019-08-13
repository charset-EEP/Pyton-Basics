#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora=float(input(print("Quanto você ganha /hora?")))
trabalho=int(input(print("Quantas horas você trabalha /mês?")))
salario=hora*trabalho
print("Salario: R$"+str(salario))
