'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

from collections import Counter
votos=[]
i=0
opcoes=["Windows Server","Unix","Linux","Netware","Mac OS","Outro"]
print("Qual o melhor Sistema Operacional para uso em servidores?")
while 0 not in votos:    
    votos.append(int(input(print("N° Sistema (0=fim):"))))
    if votos[i]!=0:
        while votos[i] not in range(1,7):
            votos[i]=(int(input(print("Informe um valor entre 1 e 7 ou 0 para sair!"))))
    i+=1
votos.pop()
c=Counter(votos)
print("""Resultado da votação:

Foram computados """+str(len(votos))+""" votos.""")
print("SO   Votos   %")
for i in range(1,6):
    
    porc=(c[i]/len(votos))*100
    print(str(opcoes[i])+ " : "+str(c[i])+" : "+str(porc)+"%")
print("TotalVotos : "+str(len(votos)))


