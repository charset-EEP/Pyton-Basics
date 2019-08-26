#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

alt=1
peso=1
alto=0
baixo=10000
gordo=0
magro=10000

while 0 not in [alt,peso]:
    alt=float(input())
    if alt !=0:
        peso=float(input())
        if alt>alto:
            alto=alt
        if alt<baixo:
            baixo=alt
        if peso>gordo:
            gordo=peso
        if peso<magro:
            magro=peso
print(alto)
print(baixo)
print(gordo)
print(magro)
        
