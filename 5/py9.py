#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


def reverso(n):
    reverso=sorted(str(n),reverse=True)
    print(*reverso,sep="")

reverso(445)
