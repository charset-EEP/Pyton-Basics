#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho=int(input(print("Qual tamanho do arquivo?em(MB)")))
internet=int(input(print("Qual velociade da internet?em(Mbps)")))
tempo=(tamanho/internet)/60
print("Tempo download: "+str(tempo)+"seg")


