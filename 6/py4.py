"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""

nome=input()
x=[]
for i in range(len(nome)+1):
    for j in range(i):
        x.append(nome[j])
    print(*x,sep="")
    x=[]
