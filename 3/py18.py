#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

num=[]
n=int(input(print("Range")))
maior=0
menor=999999999999
total=0
for i in range(n):
    num.append(int(input(print("Num:"))))
    if num[i]>maior:
        maior=num[i]
    if num[i]<menor:
        menor=num[i]
    total+=num[i]
print(total)
print(maior)
print(menor)
