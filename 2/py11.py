'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
    '''

salarioI=float(input(print("Digite seu salário")))

if salarioI<=280 :
    aumento = 20
elif salarioI>280 & salarioI<=700 :
    aumento = 15
elif salarioI>700 & salarioI<=1500 :
    aumento = 10
elif salarioI>1500 :
    aumento = 5

reajuste=salarioI*aumento/100
salarioF=salarioI + reajuste

print("Salario Antes: "+str(salarioI))
print("% Reajuste: "+str(aumento))
print("Valor Reajuste: "+str(reajuste))
print("Salario Depois: "+str(salarioF))
