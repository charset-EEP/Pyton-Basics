#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

vetor=[]
print("Digite suas notas para calcular a media")
for i in range(4):
    vetor.append(float(input()))
media=sum(vetor)/4
print(media)
