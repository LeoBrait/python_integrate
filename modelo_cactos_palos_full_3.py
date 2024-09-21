from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
#from sympy import *


# parâmetros
# taxa_associacao = 3 #c
# r_cacto_adulto = 0.006 #r1
# taxa_facilitacao = 5 #f
# taxa_envelhecimento = 0.02 #alpha (escala de 10^-2)
# k_cacto_adulto = 0.009 #k1 )(inversamente proporcional)
# morte_cacto_adulto = 0.02  #d
# r_arbusto = 3 #r2
# k_arbusto = 10 #k2
# taxa_saciedade = 1 #h
# taxa_predacao = 2 #m k 1 =< m =< 2.6


parametros_controle_1 = (
  1, 
  0.006, 
  5, 0.1, 0.009, 0.05, 3, 10, 1, 3
)

parametros_controle_2 = (
  1, 0.006, 1, 0.02, 0.009, 0.02, 3, 10, 1, 10
)

parametros_oscilatorio_ultra = (
  3, 0.006, 5, 0.02, 0.009, 0.02, 3, 10, 1, 2
)

parametros_cactos_jovens_estabilizam_acima = (
  2, 0.006, 5, 0.02, 0.009, 0.02, 3, 10, 1, 2
)

parametros_oscilatorio = (
  2, 0.006, 5, 0.02, 0.009, 0.02, 3, 10, 1, 3
)

parametros_estavel = (
  0.5, 0.009, 3, 0.05, 0.009, 0.01, 3, 10, 1, 0.6
)

# condições iniciais
x_inicial_1 = 0.1
x_inicial_2 = 0
x_inicial_3 = 10



# analise de pontos fixos

# passos de tempo
t = arange(0, 5000, 0.001)

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

################################# Modelos ######################################
modelo_estabilizado = odeint(
    modele_facilitacao_amensalismo, 
    [x_inicial_1, x_inicial_2, x_inicial_3], 
    t, 
    parametros_estavel
    )

modelo_oscilatorio = odeint(
    modele_facilitacao_amensalismo, 
    [x_inicial_1, x_inicial_2, x_inicial_3], 
    t, 
    parametros_oscilatorio
    )

#############################Plotagem de interação #############################

#  estabilizado ----------------------------------------------------------------
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_estabilizado, linewidth = 2.5, linestyle = "-")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(
  ["Cactos Recrutados (jovens)", "Cactos Adultos", "Palos Verdes"], 
  fontsize = 16
)
savefig("integrado_estavel.png")
print(modelo_estabilizado)

# Oscilatório -----------------------------------------------------------------
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_oscilatorio, linewidth = 2.5, linestyle = "-")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(
  ["Cactos Recrutados (jovens)", "Cactos Adultos", "Palos Verdes"], 
  fontsize = 16
)
savefig("integrado_oscilatorio.png")
print(modelo_oscilatorio)

######################### Espaço de fase #######################################

# Estabilizado -----------------------------------------------------------------

# 3D
# Plota o espaço de fase tridimensional
fig = figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(
  modelo_estabilizado[:, 0],
  modelo_estabilizado[:, 1],
  modelo_estabilizado[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
ax.set_xlabel("Cactos Recrutados (jovens)", fontsize=20)
ax.set_ylabel("Cactos Adultos", fontsize=20)
ax.set_zlabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_3d_estabilizado.png")

# 2D
figure(figsize=(10, 8))
plot(
  modelo_estabilizado[:, 1],
  modelo_estabilizado[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
xlabel("Cactos Adultos", fontsize=20)
ylabel("Palos Verdes", fontsize=20)


# Salvando a figura
savefig("espaco_de_fase_2d_estabilizado.png")

# Oscilatório ------------------------------------------------------------------

# 3D
# Plota o espaço de fase tridimensional
fig = figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(
  modelo_oscilatorio[:, 0],
  modelo_oscilatorio[:, 1],
  modelo_oscilatorio[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
ax.set_xlabel("Cactos Recrutados (jovens)", fontsize=20)
ax.set_ylabel("Cactos Adultos", fontsize=20)
ax.set_zlabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_3d_oscilatorio.png")

# 2D
figure(figsize=(10, 8))
plot(
  modelo_oscilatorio[:, 1],
  modelo_oscilatorio[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
xlabel("Cactos Adultos", fontsize=20)
ylabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_2d_oscilatorio.png")

################################ Diagrama de bifurcação ########################
# figure(figsize=(10, 8))
# plot(10, modelo_integrado[-5000:, 0].min(), 'ro', markersize=10)
# plot(10, modelo_integrado[-5000:, 0].max(), 'ro', markersize=10)
# plot(10, modelo_integrado[-5000:, 1].min(), 'ob', markersize=10)
# plot(10, modelo_integrado[-5000:, 1].max(), 'ob', markersize=10)
