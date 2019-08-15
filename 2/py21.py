'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

saque=int(input(print("Quanto deseja sacar?")))
if saque in range(10,600):
    resto=saque
    if saque > 100:
        nota100 = int(saque/100)
        resto = resto - (nota100*100)
        print("Notas 100: "+ str(nota100))
    if resto > 50:
        nota50 = int(resto/50)
        resto = resto - (nota50*50)
        print("Notas 50: "+ str(nota50))
    if resto > 10:
        nota10 = int(resto/10)
        resto = resto - (nota10*10)
        print("Notas 10: "+ str(nota10))
    if resto > 5:
        nota5 = int(resto/5)
        resto = resto - (nota5*5)
        print("Notas 5: "+ str(nota5))
    if resto >= 1:
        nota1 = int(resto/1)
        resto = resto - (nota1*1)
        print("Notas 1: "+ str(nota1))    
else:
    print("Valor Inválido")
