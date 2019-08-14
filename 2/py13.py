'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

dic={1:"Domingo",2:"Segunda",3:"Terça",4:"Quarta",5:"Quinta",6:"Sexta",7:"Sabado"}
i=int(input(print("Qual dia da semana quer saber?")))
print(dic[i])
