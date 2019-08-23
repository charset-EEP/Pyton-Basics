"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.

    Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
    necessita da esfera;
    necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório: 

Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
"""

print("""
Legenda
1- necessita da esfera                  
2- necessita de limpeza                 
3- necessita troca do cabo ou conector  
4- quebrado ou inutilizado 
""")
from collections import Counter
mouse=[]
i=0
perc=0
problemas=["necessita da esfera","necessita de limpeza","necessita troca do cabo ou conector","quebrado ou inutilizado"]
while 0 not in mouse:
    mouse.append(int(input(print("Estado do mouse:"))))
    i+=1
    if i==200:
        break
mouse.pop()
c=Counter(mouse)
print(c)
for i in range(4):
    perc=(c[i]/len(mouse))*100
    j=i+1
    print(str(j)+"- "+str(problemas[i])+"   "+str(c[i])+"    "+str(perc)+"%")
