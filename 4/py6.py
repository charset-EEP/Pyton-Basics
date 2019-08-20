#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

alunos=[]
j=0
for i in range(2):
    nota=0
    print("Digite as notas")
    for i in range (4):
        nota+=float(input())
    media=nota/4
    alunos.append(media)
print("Alunos com a média >7")
for i in range(2):
    if alunos[i]>=7:
        j+=1
print(j)

