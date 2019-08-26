#Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

cpf=input()
errado=0
if len(cpf)>14:
    errado+=1
if cpf[3]!=".":
    errado+=1
if cpf[7]!=".":
    errado+=1
if cpf[11]!="-":
    errado+=1
if errado>0:
    print("Errado")
    print(errado)
else:
    print("certo")
