#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idade=[]
altura=[]
j=0
for i in range(30):
    idade.append(int(input()))
    altura.append(int(input()))

alt13=[]
for i in range(30):
    if idade[i]>=13:
        alt13.append(altura[i])
k=len(alt13)
media=sum(alt13)/k
for i in range(k):
    if alt13[i]<media:
        j+=1
print(j)
