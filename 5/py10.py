#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint
def craps():
    i=0
    fim=0
    while fim==0:
        dado1=randint(1,6)
        dado2=randint(1,6)
        tot=dado1+dado2
        if i==0:
            if tot in [7,11]:
                print("Natural | GANHOU !")
                print(tot)
                fim=1
            elif tot in [2,3,12]:
                print("Craps | Perdeu")
                print(tot)                
                fim=1
            else:
                print("Ponto")
                print(tot)
                ponto=tot
        else:
            if tot==7:
                print("Perdeu")
                print(tot)
                fim=1
            elif tot==ponto:
                print("Ganhou")
                print(tot)
                fim=1
        i+=1
craps()
