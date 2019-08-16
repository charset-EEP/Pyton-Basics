#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

A=int(input(print("População da cidade A")))
cresA=float(input(print("Taxa de crescimento A")))
B=int(input(print("População cidade B")))
cresB=float(input(print("Txa de crecimento B")))
ano=0
while A!=B:
    A=A+(A*(cresA/100))
    B=B+(B*(cresB/100))
    ano+=1
print(ano)
    

