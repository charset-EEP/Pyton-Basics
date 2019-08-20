#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

altura=[]
idade=[]
for i in range(5):
    altura.append(float(input()))
    idade.append(float(input()))
ii=idade.sort(reverse=True)
aa=altura.sort(reverse=True)
print(ii)
print(aa)
