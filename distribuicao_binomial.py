import math

def binomial_distribuition(x,n,p): #
        return  (math.factorial(n)/(math.factorial(n-x)* math.factorial(x)))*(p**x)*((1-p)**(n-x))

n=160 #numero de amostras
p=0.125 #probabilidade dada

sum = 0
for i in range(n+1):
    prob = binomial_distribuition(i,n,p)
    if i>=18 and i<25:
          sum+=prob
    print(str(i)+" -> ",prob)

print("sum",sum)