"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

print("Compara duas strings")
str1=input()
str2=input()
if len(str1)==len(str2):
    print("Tamanhos Iguais")
    if str1==str2:
        print("Conteudo Igual")
    else:
        print("Conteudo Diferente")
else:
    print("Tamanhos diferentes")
    print("Conteudo Diferente")
