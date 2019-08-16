'''
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';
'''
    
nome=input(print("Nome:"))
while len(nome)<3:
    print("Digite Novamente")
    nome=input(print("Nome:"))
idade=int(input(print("Idade")))
while idade not in range(150):
    print("Digite Novamente")
    idade=int(input(print("Idade")))
salario=float(input(print("Salário:")))
while salario<0:
    print("Digite Novamente")
    salario=float(input(print("Salário:")))
sexo=input(print("Gênero"))
while sexo not in ["f","m"]:
    print("Digite Novamente")
    sexo=input(print("Gênero"))
civil=input(print("Estado civil"))
while civil not in ['s', 'c', 'v', 'd']:
    print("Digite Novamente")
    civil=input(print("Estado civil"))
