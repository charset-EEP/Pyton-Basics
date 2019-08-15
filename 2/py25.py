'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
resp1=input(print("Telefonou para a vítima?"))
resp2=input(print("Esteve no local do crime?"))
resp3=input(print("Mora perto da vítima?"))
resp4=input(print("Devia para a vítima?"))
resp5=input(print("Já trabalhou com a vítima?"))
cont=0
if resp1=="sim": cont+=1
if resp2=="sim": cont+=1
if resp3=="sim": cont+=1
if resp4=="sim": cont+=1
if resp5=="sim": cont+=1

if cont in [0,1]:
    print("Inocente")
if cont == 2:
    print("Suspeito")
if cont in [3,4]:
    print("Cúmplice")
if cont == 5:
    print("Assassino")
