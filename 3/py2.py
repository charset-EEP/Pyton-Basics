#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario=input(print("Digite seu nome de usuário"))
senha=input(print("Digite sua senha"))
while usuario==senha:
    print("ERRO")
    usuario=input(print("Digite seu nome de usuário"))
    senha=input(print("Digite sua senha"))
