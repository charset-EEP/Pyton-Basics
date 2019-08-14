'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 
'''

a=int(input(print("Digite o valor de A")))
if a>0:
    b=int(input(print("Digite o valor de B")))
    c=int(input(print("Digite o valor de C")))
    delta=(b*b)-4*a*c
    if delta>=0:
        if delta==0:
            print("Delta igual a zero, possui 1 raiz")
            x1=(-(b))/(2*a)
            x2="NA"
        else:
            print("Delta positivo, possui 2 raizes")
            x1=(-(b)+(delta**(1/2)))/(2*a)
            x2=(-(b)-(delta**(1/2)))/(2*a)
        print(x1)
        print(x2)
    else:
        print("Delta negativo")
