#Faça um programa que calcule o mostre a média aritmética de N notas.

n=int(input(print("Total")))
notatot=0
for i in range(n):
    nota=float(input(print("Nota")))
    notatot+=nota
media=notatot/n
print(media)
