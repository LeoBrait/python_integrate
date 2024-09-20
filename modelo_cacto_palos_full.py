from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 1
r2 = 0.1
k1 = 10
k2 = 1000
x_inicial_1 = 0
x_inicial_2 = 0
x_inicial_3 = 100
taxa_transicao = 0
cacto_death = 0.1
taxa_predacao = 0
taxa_facilitacao = 1

# passos de tempo
t = arange(0, 100., 0.01)

def modele_facilitacao_amensalismo(
  x, t, r1, k1, r2, k2, taxa_transicao,
  cacto_death, taxa_predacao, taxa_facilitacao):
  
  return array([
   x[1] * (r1 + taxa_facilitacao * x[2]) - taxa_transicao * x[0],
   taxa_transicao * x[0] - cacto_death * x[1] - k1 * (x[1] ** 2),
   r2 * x[2] * (1 - x[2] / k2) - taxa_predacao
  ])

#r2 * x[1] * ( 1 - x[1] / k2)


modelo_integrado = odeint(modele_facilitacao_amensalismo, [x_inicial_1, x_inicial_2, x_inicial_3], t, (r1, k1, r2, k2, taxa_transicao, cacto_death, taxa_predacao, taxa_facilitacao))

# plotando a solução
figure(figsize=(8, 6))
tick_params(labelsize= 15)
plot(t, modelo_integrado,linewidth=2.5)
xlabel('t',fontsize=20) # definir rótulo do eixo x
ylabel('x',fontsize = 20) # e do eixo y
legend(['Cactos', 'cactos_facilitados', 'Palos'],fontsize=16)
savefig("full_model.png")
