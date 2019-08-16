#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

num = -1
while num not in range(10) :
    num = int(input(print("Digite um numero entre 0~10")))
    
