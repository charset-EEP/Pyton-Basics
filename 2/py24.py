'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.
'''
n1=float(input(print("Digite 1° numero")))
n2=float(input(print("Digite 2° numero")))
operacao=input(print("Qual operação deseja realizar?"))
if operacao == "+":
    resultado=n1+n2
elif operacao == "-":
    resultado=n1-n2
elif operacao == "*":
    resultado=n1*n2
elif operacao == "/":
    resultado=n1/n2
else : print("erro")
print(resultado)
if ".0" in str(resultado):
    print("Int")
else:
    print("Float")
if resultado>0:
    print("Positivo")
else:
    print("Negativo")
if resultado%2==0:
    print("Par")
else:
    print("Impar")
