#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. 

num=int(input(print("Num: ")))
for i in range(num):
    if i>1:
        if num%i==0:
            print("N-Primo")
            quit()
print("Primo")
