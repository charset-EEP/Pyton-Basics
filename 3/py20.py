#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 

num=(int(input(print("Num:"))))
if num<16:
    for i in range(num):
        if i>0:
            num=num*i
print(num)

