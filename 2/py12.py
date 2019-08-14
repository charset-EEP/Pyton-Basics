'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220
'''

horaS=float(input(print("Quanto você ganha por hora?")))
horaT=float(input(print("Quantas horas você trabalhou no mês?")))

salarioB=horaT*horaS

if salarioB<=900:
    porc = 0
elif salarioB in range(900,1500) :
    porc = 5
elif salarioB in range(1500,2500):
    porc = 10
else :
    porc = 20


IR=(porc/100)*salarioB
INSS=(10/100)*salarioB
sindicato=(11/100)*salarioB
salarioL=salarioB-IR-INSS

print("+ Salário Bruto : R$"+str(salarioB))
print("- IR (11%) : R$"+str(IR))
print("- INSS (10%) : R$"+str(INSS))
print(" FGTS ( 11%) : R$"+str(sindicato))
print("= Salário Liquido : R$"+str(salarioL))

