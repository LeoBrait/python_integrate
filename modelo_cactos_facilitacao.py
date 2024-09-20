from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

# parâmetros
r1 = 2.
r2 = 3.
k1 = 10.
k2 = 20.
x_inicial_1 = 0.1
x_inicial_2 = 0.1

# passos de tempo
t = arange(0, 10., 0.01)

######################### Modelo Logístico (cactos solitarios) #################
def logistico_cactos(x, t, r1, k1):
  return r1 * x * ( 1 - x / k1 )

logistico_cactos_integrado = odeint(logistico_cactos, x_inicial_1, t, (r1, k1))


######################### Modelo Logítico Palos ################################
def logistico_palos(x, t, r2, k2):
  return r2 * x * ( 1 - x / k2 )

logistico_palos_integrado = odeint(logistico_palos, x_inicial_2, t, (r2, k2))

##################### Modelo Logístico de Cactos facilitados por Palos #########
def logistico_cactos_facilitados(x, t, r1, k1, r2, k2, a = 3):
  return array([
    r1 * (x[0] + x[0] * a * x[1]) * ( 1 - x[0] / k1),
    r2 * x[1] * ( 1 - x[1] / k2)
 ])

logistico_cactos_facilitados_integrado = odeint(logistico_cactos_facilitados, [x_inicial_1, x_inicial_2], t, (r1, k1, r2, k2))



############################### Plot Modelo Logístico ##########################
# plotando a solução
figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
plot(t, logistico_cactos_integrado,linewidth=2.5)
plot(t, logistico_palos_integrado,linewidth=2.5)
plot(t, logistico_cactos_facilitados_integrado[:,0],linewidth=2.5)
xlabel('t',fontsize=20) # definir rótulo do eixo x
ylabel('x',fontsize = 20) # e do eixo y
legend(['Cactos', 'Palos', 'Cactos facilitados por Palos'],fontsize=16)
savefig("logistico.png")