from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
#from sympy import *


####################### Parâmetros do modelo ###################################

# taxa_associacao (c)
# r_cacto_adulto = (r1)
# taxa_facilitacao = (f)
# taxa_envelhecimento = (alpha) (escala de 10^-2)
# k_cacto_adulto = (k1) (inversamente proporcional)
# morte_cacto_adulto = (d)
# r_arbusto = (r2)
# k_arbusto = (k2)
# taxa_saciedade = (h)
# taxa_predacao = (m) k 1 =< m =< 2.

# parametros fixos
taxa_associacao = 0.8
r_cacto_adulto = 0.009
taxa_envelhecimento = 1/35
k_cacto_adulto = 2/100
morte_cacto_adulto = 0.3
r_arbusto = 1
k_arbusto = 50
taxa_saciedade = 0.8
taxa_predacao = 1.5

parametros_facilitacao_0 = (
  taxa_associacao, # taxa_associacao
  r_cacto_adulto, # r_cacto_adulto
  0, # taxa de facilitacao
  taxa_envelhecimento, # taxa de envelhecimento dos cactos (35 anos para envelhecer)
  k_cacto_adulto, # k do cacto adulto (50 cactos)
  morte_cacto_adulto, # 0.3 cactos morrem naturalmente por ano
  r_arbusto, # r do arbusto
  k_arbusto, # 50 cactos
  taxa_saciedade, # taxa de saciedade (os cactos matam 0.8 arbustos por ano)
  taxa_predacao # taxa de predacao (adimensional
)

parametetros_facilitacao_1 = (
  taxa_associacao, # taxa_associacao
  r_cacto_adulto, # r_cacto_adulto
  1, # taxa de facilitacao
  taxa_envelhecimento, # taxa de envelhecimento dos cactos (35 anos para envelhecer)
  k_cacto_adulto, # k do cacto adulto (50 cactos)
  morte_cacto_adulto, # 0.3 cactos morrem naturalmente por ano
  r_arbusto, # r do arbusto
  k_arbusto, # 50 cactos
  taxa_saciedade, # taxa de saciedade (os cactos matam 0.8 arbustos por ano)
  taxa_predacao # taxa de predacao (adimensional
)
  

# condições iniciais
x_inicial_1 = 0.1
x_inicial_2 = 0
x_inicial_3 = 10


# passos de tempo
t = arange(0, 5000, 0.01)

################################# Modelo #######################################
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
modelo_facilitacao_0 = odeint(
    modele_facilitacao_amensalismo,
    [x_inicial_1, x_inicial_2, x_inicial_3],
    t,
    parametros_facilitacao_0
)

modelo_facilitacao_1 = odeint(
    modele_facilitacao_amensalismo,
    [x_inicial_1, x_inicial_2, x_inicial_3],
    t,
    parametetros_facilitacao_1
)

#############################Plotagem de integracao ############################

#  facilitacao 0 ---------------------------------------------------------------
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_facilitacao_0, linewidth = 2.5, linestyle = "-")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(
  ["Cactos Recrutados (jovens)", "Cactos Adultos", "Palos Verdes"], 
  fontsize = 16
)
savefig("integrado_facilitacao_0.png")
print(modelo_facilitacao_0)

# facilitacao 1 ---------------------------------------------------------------
figure(figsize = (8, 6))
tick_params(labelsize = 15)
plot(t, modelo_facilitacao_1, linewidth = 2.5, linestyle = "-")
xlabel("t", fontsize = 20) # definir rótulo do eixo x
ylabel("x", fontsize = 20) # e do eixo y
legend(
  ["Cactos Recrutados (jovens)", "Cactos Adultos", "Palos Verdes"],
  fontsize = 16
)
savefig("integrado_facilitacao_1.png")
print(modelo_facilitacao_1)


######################### Espaço de fase #######################################

# facilitacao 0 ---------------------------------------------------------------
# 3D
fig = figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(
  modelo_facilitacao_0[:, 0],
  modelo_facilitacao_0[:, 1],
  modelo_facilitacao_0[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
ax.set_xlabel("Cactos Recrutados (jovens)", fontsize=20)
ax.set_ylabel("Cactos Adultos", fontsize=20)
ax.set_zlabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_3d_facilitacao_0.png")

# 2D
figure(figsize=(10, 8))
plot(
  modelo_facilitacao_0[:, 1],
  modelo_facilitacao_0[:, 2],
  linewidth = 2.5,
  linestyle = "-"
)

# Definindo rótulos dos eixos
xlabel("Cactos Adultos", fontsize=20)
ylabel("Palos Verdes", fontsize=20)


# Salvando a figura
savefig("espaco_de_fase_2d_facilitacao_0.png")

# facilitacao 1 ---------------------------------------------------------------

# 3D -----------------------------------
fig = figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(
  modelo_facilitacao_1[:, 0],
  modelo_facilitacao_1[:, 1],
  modelo_facilitacao_1[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
ax.set_xlabel("Cactos Recrutados (jovens)", fontsize=20)
ax.set_ylabel("Cactos Adultos", fontsize=20)
ax.set_zlabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_3d_facilitacao_1.png")

# 2D -----------------------------------
figure(figsize=(10, 8))
plot(
  modelo_facilitacao_1[:, 1],
  modelo_facilitacao_1[:, 2],
  linewidth = 2.5, 
  linestyle = "-"
)

# Definindo rótulos dos eixos
xlabel("Cactos Adultos", fontsize=20)
ylabel("Palos Verdes", fontsize=20)

# Salvando a figura
savefig("espaco_de_fase_2d_facilitacao_1.png")


################################ Diagrama de bifurcação ########################

## este bloco calcula soluções para muitos K's, devemos criar listas 
#  vazia para  que possamos anexar os valores posteriormente
ymin = []
ymax = []
ff = arange(0, 20, .01)
t = arange(0, 10000, 0.1)

for f in ff:

    parametros =  (
      taxa_associacao, # taxa_associacao
      r_cacto_adulto, # r_cacto_adulto
      f, # taxa de facilitacao
      taxa_envelhecimento, # taxa de envelhecimento dos cactos (35 anos para envelhecer)
      k_cacto_adulto, # k do cacto adulto (50 cactos)
      morte_cacto_adulto, # 0.3 cactos morrem naturalmente por ano
      r_arbusto, # r do arbusto
      k_arbusto, # 50 cactos
      taxa_saciedade, # taxa de saciedade (os cactos matam 0.8 arbustos por ano)
      taxa_predacao # taxa de predacao (adimensional
    )
    #integre novamente a equação, com novos parâmetros
    y = odeint(modele_facilitacao_amensalismo, [x_inicial_1, x_inicial_2, x_inicial_3], t, parametros)
    ymin.append(y[-1000:,:].min(axis=0))
    ymax.append(y[-1000:,:].max(axis=0))

# converte as listas em arrays
ymin = array(ymin)
ymax = array(ymax)




figure(figsize=(10, 8))
plot(ff, ymin[:,1], "g", linewidth = 2.5, linestyle = "-")
plot(ff, ymin[:,2], "b", linewidth = 2.5, linestyle = "-")
plot(ff, ymax[:,1], "g", linewidth = 2.5, linestyle = "-")
plot(ff, ymax[:,2], "b", linewidth = 2.5, linestyle = "-")
xlabel("facilitacao", fontsize = 20)
ylabel("população min / max", fontsize = 20)
legend(loc = "best", fontsize = 16)
yscale("log")
legend(
  ["Cactos Adultos Mínimo", "Palos Verdes Mínimo", "Cactos Adultos Máximo", "Palos Verdes Máximo"], 
  fontsize = 16
)

savefig("diagrama_de_bifurcacao.png")


