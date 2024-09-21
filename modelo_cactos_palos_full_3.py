from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
taxa_associacao = 3 #c
r_cacto_adulto = 0.006 #r1
taxa_facilitacao = 5 #f
taxa_envelhecimento = 0.02 #alpha (escala de 10^-2)
k_cacto_adulto = 0.009 #k1 )(inversamente proporcional)
morte_cacto_adulto = 0.02  #d
r_arbusto = 3 #r2
k_arbusto = 10 #k2
taxa_saciedade = 1 #h
taxa_predacao = 2 #m k

# condições iniciais
x_inicial_1 = 0.1
x_inicial_2 = 0
x_inicial_3 = 10

# analise de pontos fixos

# passos de tempo
t = arange(0, 1000, 0.001)

def modele_facilitacao_amensalismo(
    x, t,
    taxa_associacao, r_cacto_adulto, 
    taxa_facilitacao, taxa_envelhecimento, 
    k_cacto_adulto, morte_cacto_adulto, 
    r_arbusto, k_arbusto, taxa_saciedade, 
    taxa_predacao):
  
  return array([
  
  # Cactos Baby =
  taxa_associacao * r_cacto_adulto * (taxa_facilitacao * x[2]) * x[1] + (1 - taxa_associacao) * r_cacto_adulto * x[1] - taxa_envelhecimento * x[0],
  
  # Cactos Adultos =
  taxa_envelhecimento * x[0] - k_cacto_adulto * (x[1] ** 2) - morte_cacto_adulto * x[1],
  
  
  # Arbustos =
  r_arbusto * x[2] * (1 - (x[2] / k_arbusto)) - ((taxa_associacao * x[1] * x[2]) /(1 + taxa_saciedade * x[1])) * taxa_predacao
  ])




modelo_integrado = odeint(
    modele_facilitacao_amensalismo, 
    [x_inicial_1, x_inicial_2, x_inicial_3], 
    t, 
    (taxa_associacao, r_cacto_adulto, taxa_facilitacao, taxa_envelhecimento, k_cacto_adulto, morte_cacto_adulto, r_arbusto, k_arbusto, taxa_saciedade, taxa_predacao)
    )

# plotando a solução
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_integrado, linewidth = 2.5, linestyle = "-")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(["Cactos Recrutados (jovens)", "Cactos Adultos", "Palos Verdes"], fontsize = 16)
savefig("full_model_3.png")
print(modelo_integrado)
