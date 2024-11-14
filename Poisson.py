import math
e = math.exp(1) #define euler

def Poisson(contagem,x):
    return ((e**(-contagem))*(contagem**(x)))/math.factorial(x)

sum = 0
for i in range(10):
    p=Poisson(6,i)
    if (i>=6)and(i<10):
        sum+=p
    print(i,"->",p)
print(sum)

