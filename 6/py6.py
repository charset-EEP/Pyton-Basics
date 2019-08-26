"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.
"""

def data(data):
    if data[3]=="1":
        if data[4]=="0":
            print("Outubro")
        elif data[4]=="1":
            print("Novembro")
        elif data[4]=="2":
            print("Dezembro")
    else:
        if data[4]=="1":
            print("Janeiro")
        elif data[4]=="2":
            print("Fevereiro")
        elif data[4]=="3":
            print("Março")
        elif data[4]=="4":
            print("Abril")
        elif data[4]=="5":
            print("Maio")
        elif data[4]=="6":
            print("Junho")
        elif data[4]=="7":
            print("Julho")
        elif data[4]=="8":
            print("Agosto")
        elif data[4]=="9":
            print("Setembro")
        
data("01/01/2000")
data("01/02/2000")
data("01/03/2000")
data("01/04/2000")
data("01/05/2000")
data("01/06/2000")
data("01/07/2000")
data("01/08/2000")
data("01/09/2000")
data("01/10/2000")
data("01/11/2000")
data("01/12/2000")
