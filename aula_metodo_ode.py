from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r = 2.
K = 10.
x0 = 0.1

# jumps
t = arange(0, 10., 0.01)

# a função que descreve a equação diferencial
def f(x, t, r, K):
  return r * x * (1-x/K)

x = odeint(f, x0, t, (r, K))

# plotando a solução
# figure(figsize=(8, 6)) 
# tick_params(labelsize= 15)
# plot(t, x, linewidth=5, linestyle='--')
# xlabel('t',fontsize=20) # definir rótulo do eixo x
# ylabel('x',fontsize=20) # e do eixo y

# plotar solução analítica
# note que `t` é um array: quando você faz qualquer operação aritmética
# com um array, é o mesmo que fazer para cada elemento
plot(
  t, 
  K * x0 * exp(r*t)/(K+x0*(exp(r*t)-1.)),
  linewidth=2.5
)
legend(['aproximação', 'solução analítica'], loc='best',fontsize=20) # draw legend

# salvar a figura
savefig('test.png')