"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

palavra=input()
branco=0
vogal=0
for i in range(len(palavra)):
    if(palavra[i]==" "):
        branco+=1
    if palavra[i] in ["a","e","i","o","u"]:
        vogal+=1
print(branco)
print(vogal)
