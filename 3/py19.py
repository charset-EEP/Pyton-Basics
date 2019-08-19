#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

num=[]
n=int(input(print("Range")))
maior=0
menor=1000
total=0
x=0
for i in range(n):
    while x not in range(1,1001):
        x=int(input(print("Num:")))
    num.append(x)
    if num[i]>maior:
        maior=num[i]
    if num[i]<menor:
        menor=num[i]
    total+=num[i]
print(total)
print(maior)
print(menor)

