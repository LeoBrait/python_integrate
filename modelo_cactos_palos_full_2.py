from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 1
r2 = 1
k1 = 10
k2 = 10
x_inicial_1 = 0
x_inicial_2 = 100
x_inicial_3 = 100
taxa_transicao = 0.5
cacto_death = 0.1
taxa_predacao = 0
taxa_facilitacao = 1

# passos de tempo
t = arange(0, 100., 0.01)

def modele_facilitacao_amensalismo(
  x, t, r1, k1, r2, k2, taxa_transicao,
  cacto_death, taxa_predacao, taxa_facilitacao):
  
  return array([
  
  # Cactos Nascidos =
  # (taxa de crescimento[r_base]) * (cactos adultos)
  
  # Cactos Recrutados = 
  # (taxa de crescimento) * (cactos adultos) [rectrutados] 
  # + (taxa de facilitação) * (arbustos) * (cactos adultos) [incremento no recrutamento por facilitacao]
  # - (taxa de transição) * (cactos recrutados) [transição de recrutados para adultos
  # PROBLEMA: O recrutmento ta instantaneo. Falta uma saciedade para a transição de cactos recrutados para cactos adultos.
  r1 * x[1] + (taxa_facilitacao * x[2] * x[1]) -  taxa_transicao * x[0],
  
  # Cactos Adultos =
  #(recrutados convertidos) - (mortes_naturais) * (suporte)
  taxa_transicao * x[0] - cacto_death * x[1] - k1 * (x[1] ** 2),
  
  # Arbustos = 
  r2 * x[2] * (1 - x[2] / k2) #- taxa_predacao
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
savefig("full_model.png")
