"""
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

    para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def piramide(n):
    m=n+1
    for i in range(m):
        k=i+1
        for j in range(k):
            print(j,end=" ")
        print("")
piramide(5)
