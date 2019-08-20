#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.

i=0
tot=0
maior=0
menor=5000
while 1:
    temp=float(input(print("Temp")))
    tot+=temp
    i+=1
    if temp>maior:
        maior=temp
    if temp<menor:
        menor=temp    
    if temp==-1:
        break
media=tot/i
print(media)
print(maior)
print(menor)
