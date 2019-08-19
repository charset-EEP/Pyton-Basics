#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n=int(input(print("Tot")))
n=n+1
for num in range(n):
    x=0
    for i in range(num):
        if i>1:
            if num%i==0:
                x=0
                break
            else:
                x+=1
    if num in range(1,4):
        print(str(num)+" Primo")
    if x>2:
        print(str(num)+" Primo")
        


