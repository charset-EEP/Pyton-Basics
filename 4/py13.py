#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temp=[]
for i in range(12):
    temp.append(int(input()))
media=sum(temp)/12
for i in range(12):
    if temp[i]>media:
        print(temp[i])
