# série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500. 

num=[]
n=500
n=n+1
for i in range(n):
    if i>2:
        a=i-1
        b=i-2
        c=num[a]+num[b]
        num.append(c)
    else:
        num.append(1)
num[0]=0
print(num)
