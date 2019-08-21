'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''
nome="a"
saltos=[]
while nome!="":
    nome = input(print("Nome"))
    if nome!="":
        for i in range(5):
            saltos.append(float(input(print("Salto"))))
        print("Atleta: "+nome)
        print("Primeiro Salto: "+str(saltos[0])+" m")
        print("Segundo Salto: "+str(saltos[1])+" m")
        print("Terceiro Salto: "+str(saltos[2])+" m")
        print("Quarto Salto: "+str(saltos[3])+" m")
        print("Quinto Salto: "+str(saltos[4])+" m")
        print("Resultado final:")
        print("Atleta: "+nome)
        print("Saltos: "+str(saltos[0])+" - "+str(saltos[1])+" - "+str(saltos[2])+" - "+str(saltos[3])+" - "+str(saltos[4]))
        media=sum(saltos)/5
        print("Média dos Saltos: "+str(media)+"m")
    
