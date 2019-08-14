#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano=int(input(print("Ano:")))

if ano%4==0:
    if ano%100==0:
        print("Não Bissesto")
    else:
        print("Bissesto")
else:
    print("Não Bissesto")

