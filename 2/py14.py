#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1=float(input(print("Digite a primeira nota")))
nota2=float(input(print("Digite a segunda nota")))
media=(nota1+nota2)/2
if media in range(9,11):
    print("A")
elif media in range(7,9):
    print("B")
elif media in range(6,7):
    print("C")
elif media in range(4,6):
    print("D")
else:
    print("E")
