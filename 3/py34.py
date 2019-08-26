#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

n=int(input())
primo=1
for i in range(n):
    if i>1:
        if n%i==0:
            primo=0
if primo==0:
    print("N-Primo")
else:
    print("primo")
