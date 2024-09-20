from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 0.1
r2 = 3
k1 = 10
k2 = 20
x_inicial_1 = 0.1
x_inicial_2 = 0.1
x_inicial_3 = 100
alpha = 1

cacto_death = 0.1


c = 0.1
f = 10

# passos de tempo
t = arange(0, 10., 0.01)

def modele_facilitacao_amensalismo(x, t, r1, k1, r2, k2, alpha,
                                   cacto_death, 
    c, f):
  return array([
   x[0] * (r1 + f * x[2]) - alpha * x[0],
   alpha * x[0] - cacto_death * x[1] - k1 * x[1] ** 2,
   r2 * x[2] * (1 - (x[2] - c * x[1] / k2) )
 ])

modelo_integrado = odeint(modele_facilitacao_amensalismo, [x_inicial_1, x_inicial_2, x_inicial_3], t, (r1, k1, r2, k2, alpha, cacto_death, c, f))

# plotando a solução
figure(figsize=(8, 6))
tick_params(labelsize= 15)
plot(t, modelo_integrado,linewidth=2.5)
xlabel('t',fontsize=20) # definir rótulo do eixo x
ylabel('x',fontsize = 20) # e do eixo y
legend(['Cactos', 'cactos_facilitados', 'Palos'],fontsize=16)
savefig("full_model.png")
