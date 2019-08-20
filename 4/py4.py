#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

vetor=[]
j=0
for i in range(10):
    letra=input()
    if letra not in ["a","e","i","o","u"]:
        vetor.append(letra)
print(vetor)
print(len(vetor))
