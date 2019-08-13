#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7 

altura=float(input(print("Digite sua altura")))
genero=input("Homem (h) ou Mulher (m)?")

if genero == "h":
    peso=(72.7*altura) - 58
elif genero == "m":
    peso=(62.1*altura) - 44.7
else:
    print("Genero errado")
    
print("Peso ideal: "+str(peso))
