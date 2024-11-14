import math
import matplotlib.pyplot as plt
e = math.exp(1) #define euler
pi = 355/113 #define pi
resolucao = 0.001 #best is 0.001 

def normal_given_X(x,med,desvpad):
    return (1/(desvpad*(math.sqrt(2*pi))))*(e**(-0.5*(((x-med)/desvpad)**2))) #funcao que retorna a probabilidade dados: x, media e desvio padrao

#########variaveis para modificar
media = 825 #media
desvio_padrao = math.sqrt(900) #desvio padrao
imin=801
imax=870
#################################

lista_prob = []
lista_i = []
sum = 0
while (imin<=imax): #loop que calcula probablilidades e soma a uma variavel que carrega a soma total
    imin = round(imin,5)
    lista_i.append(imin)
    p=round(normal_given_X(imin,media,desvio_padrao),5)
    lista_prob.append(p)
    if (imin<=imax):
        sum+=p*resolucao
    print(imin,"->",p)
    imin+=resolucao
print(round(sum,5))

#linhas abaixo criam o grafico
fig, ax = plt.subplots()
ax.plot(lista_i,lista_prob)
ax.set(xlabel='x', ylabel='f(x)',
       title='normal distribution aproximation')
ax.grid()

fig.savefig("test.png")
plt.show()