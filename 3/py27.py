#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas=int(input(print("Quantas turmas?")))
alunos=0
for i in range(turmas):
    alunos+=int(input(print("Quantos alunos?")))
media=alunos/turmas
print(media)
