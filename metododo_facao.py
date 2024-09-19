import matplotlib
from numpy import *
from matplotlib.pyplot import *

# Intervalos de tempo
tt = arange(0, 10, 0.5)
# Condição Inicial 
condicao_inicial = [0.1]

def f(x):
    return x * (1. - x)

# loop sobre o tempo
for t in tt[1:]:
    condicao_inicial.append(condicao_inicial[-1] + 0.5 * f(condicao_inicial[-1]))

# plottando
figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
plot(tt, condicao_inicial, '.-',linewidth=2.5)
ta = arange(0, 10, 0.01)
plot(ta, 0.1 * exp(ta)/(1+0.1*(exp(ta)-1.)),linewidth=2.5)
xlabel('t',fontsize=20)
ylabel('x',fontsize=20)
legend(['aproximação', 'solução analítica'], loc='best',fontsize=16)

# save figure
savefig('test.png')