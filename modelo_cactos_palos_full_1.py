from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 0.2
r2 = 0.5
k1 = 10
k2 = 20
x_inicial_1 = 10
x_inicial_2 = 10
x_inicial_3 = 10
taxa_transicao = 0.5
cacto_death = 0.1
taxa_predacao = 0.1
taxa_facilitacao = 1

# passos de tempo
t = arange(0, 500, 0.01)

def modele_facilitacao_amensalismo(
  x, t, r1, k1, r2, k2, taxa_transicao,
  cacto_death, taxa_predacao, taxa_facilitacao):
  
  return array([
  
  # Cactos Recrutados =
  (r1 + taxa_facilitacao * x[2]) *  x[1] - taxa_transicao * x[0], 
  
  # Cactos Adultos =
  taxa_transicao - cacto_death * x[1] - k1 * (x[1] ** 2),
  
  # Arbustos = 
  r2 * x[2] * (1 - (x[1] - taxa_predacao * x[1] / k2))
  ])

#r2 * x[1] * ( 1 - x[1] / k2)


modelo_integrado = odeint(modele_facilitacao_amensalismo, [x_inicial_1, x_inicial_2, x_inicial_3], t, (r1, k1, r2, k2, taxa_transicao, cacto_death, taxa_predacao, taxa_facilitacao))

# plotando a solução
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_integrado, linewidth = 2.5, linestyle = "--")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(["Cactos", "Cactos Recrutados", "Palos"], fontsize = 16)
savefig("full_model_1.png")
