'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o
    preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

tipo=input(print("Qual tipo de combustível que deseja? G/A"))
qnt=int(input(print("Quantos litros?")))
if tipo=="A":
    if qnt<=20:
        palc=1.90-((3/100)*1.90)
    else:
        palc=1.90-((5/100)*1.90)
    vpago=palc*qnt
elif tipo=="G":
    if qnt<=20:
        pgas=2.50-((4/100)*2.50)
    else:
        pgas=2.50-((6/100)*2.50)
    vpago=pgas*qnt
print(vpago)
