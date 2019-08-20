#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1=0
candidato2=0
candidato3=0
eleitores=[]
num=int(input(print("Quantos eleitores tem?")))
for i in range(num):
    voto=int(input(print("VOTO:")))
    if voto == 1:
        candidato1+=1
    elif voto == 2:
        candidato2+=1
    elif voto==3:
        candidato3+=1
print(candidato1)
print(candidato2)
print(candidato3)
