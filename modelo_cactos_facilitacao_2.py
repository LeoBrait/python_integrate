# Este é um modelo de facilitação sem conversão e sem predadores.

from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 0.2
r2 = 0.5
k1 = 10
k2 = 12
x_inicial_1 = 10
x_inicial_2 = 10
x_inicial_3 = 10
x_inicial_4 = 10
nascimento = 0.2
mortes_infantis = 0.1
a = 10


# passos de tempo
t = arange(0, 100, 0.01)


##################### Modelo Logístico de Cactos facilitados por Palos #########
def logistico_cactos_facilitados(x, t, r1, k1, r2, k2):
  return array([
    
    # Cacto Baby =
    nascimento - mortes_infantis * x[0] - k1 * (x[1] ** 2),
      
    # Cactos Recrutados = 
    # (babes vivos) + (babes vivos * taxa de facilitação * arbustos) * (babes recrutados * taxa de transição)
    x[0] + (x[0] * a * x[3]) * (x[1] - k1 * (x[1] ** 2)),
    
    # Cactos Adultos =
    # (recrutados convertidos) - (mortes_naturais) * (suporte)
    r1 * x[1] * ( 1 - x[2] / k1),
    
    # arbustos
    r2 * x[3] * ( 1 - x[3] / k2)
 ])

modelo_integrado = odeint(logistico_cactos_facilitados, [x_inicial_1, x_inicial_2, x_inicial_3, x_inicial_4], t, (r1, k1, r2, k2))

############################### Plot Modelo Logístico ##########################
# plotando a solução
figure(figsize=(8, 6)) 
tick_params(labelsize=15)
plot(t, modelo_integrado, linewidth=2.5, linestyle="--")
xlabel("t", fontsize=20) # definir rótulo do eixo x
ylabel("x", fontsize=20) # e do eixo y
legend(["Cactos baby", "Cactos Recrutados", "Cactos Adultos", "Arbustos"], fontsize=16)
savefig("facilitacao_2.png")
