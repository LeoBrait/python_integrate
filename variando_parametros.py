import matplotlib
from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
ion()

def RM(y, t, r, K, a, h, e, d):
    return array([
        y[0] * ( r*(1-y[0]/K) - a*y[1]/(1+a*h*y[0]) ),
        y[1] * (e*a*y[0]/(1+a*h*y[0]) - d) 
    ])


t = arange(0, 1000, .1)
y0 = [1, 1.]
pars =  (1., 10., 1., 0.1, 0.1, 0.1)

y = odeint(RM, y0, t, pars)

figure(figsize=(8, 6)) 
plot(t, y, linewidth=2.5)
tick_params(labelsize= 15)
xlabel('tempo',fontsize=20)
ylabel('população',fontsize=20)
legend(['recurso', 'consumidor'],fontsize=16)

# Save fig
savefig("variando.png")

figure(figsize=(8, 6)) 
# plote a solução no espaço de fase
plot(y[:,0], y[:,1],linewidth=2.5)
tick_params(labelsize= 15)
# definindo uma grade de pontos
R, C = meshgrid(arange(0.95, 1.25, .05), arange(0.95, 1.04, 0.01))
# calcula o valor da derivada no ponto na grade
dy = RM(array([R, C]), 0, *pars)
# traçamos as setas nos pontos da grade, com a diferença
# e comprimento determinado pela derivada dy
# Esta é uma imagem do fluxo da solução no espaço de fase
quiver(R, C, dy[0,:], dy[1,:], scale_units='xy', angles='xy')
xlabel('Recurso',fontsize=20)
ylabel('Consumidor',fontsize=20)

savefig("espaco_De_faase.png")


t = arange(0, 1000, .1)
pars =  (1., 15., 1., 0.1, 0.1, 0.1)
y_osc = odeint(RM, y0, t, pars)

figure(figsize=(8, 6)) 
plot(t, y_osc, linewidth=2.5)
tick_params(labelsize= 15)
xlabel('tempo',fontsize=20)
ylabel('população',fontsize=20)
legend(['recurso', 'consumidor'],fontsize=16)
savefig("oscilado.png")

figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
plot(y_osc[:,0], y_osc[:,1],linewidth=2.5)
R, C = meshgrid(arange(0, 6., .4), arange(0, 2.1, 0.2))
dy = RM(array([R, C]), 0, *pars)
quiver(R, C, dy[0,:], dy[1,:], scale_units='xy', angles='xy')
xlabel('Recurso',fontsize=20)
ylabel('Consumidor',fontsize=20)
savefig("novo_espaco_fase.png")


figure(figsize=(8, 6)) 
plot(10., y[-500:,0].min(), 'og',markersize=20)
plot(10., y[-500:,0].max(), 'og',markersize=20)
plot(10., y[-500:,1].min(), 'ob',markersize=20)
plot(10., y[-500:,1].max(), 'ob',markersize=20)
plot(15., y_osc[-500:,0].min(), 'og',markersize=20)
plot(15., y_osc[-500:,0].max(), 'og',markersize=20)
plot(15., y_osc[-500:,1].min(), 'ob',markersize=20)
plot(15., y_osc[-500:,1].max(), 'ob',markersize=20)
xlim((0, 20))
yscale('log')
tick_params(labelsize= 15)
xlabel('K',fontsize=20)
ylabel('População min / max',fontsize=20)
savefig("variando_k.png")

## este bloco calcula soluções para muitos K's, devemos criar listas 
#  vazia para  que possamos anexar os valores posteriormente
ymin = []
ymax = []
KK = arange(.5, 25, .5)
t = arange(0, 6000, 1.)
# loop sobre os valores de K (KK)
for K in KK:
    #redefine os parâmetros usando o novo K
    pars =  (1., K, 1., 0.1, 0.1, 0.1)
    #integre novamente a equação, com novos parâmetros
    y = odeint(RM, y0, t, pars)
    # calcula o mínimo e o máximo das populações, mas
    # apenas para os últimos 1000 passos (a solução a longo prazo),
    # anexando o resultado à lista
    # pergunta: 1000 é suficiente? Quando não seria?
    ymin.append(y[-1000:,:].min(axis=0))
    ymax.append(y[-1000:,:].max(axis=0))
# converte as listas em arrays
ymin = array(ymin)
ymax = array(ymax)

figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
# E agora, plotamos os diagrâmas de bifurcação
plot(KK, ymin[:,0], 'g', label='recurso',linewidth=3.5)
plot(KK, ymin[:,1], 'b', label='consumidor',linewidth=3.5)
plot(KK, ymax[:,0], 'g',linewidth=3.5)
plot(KK, ymax[:,1], 'b',linewidth=3.5)
xlabel('$K$',fontsize=20)
ylabel('Populações min/max',fontsize=20)
legend(loc='best')
# Usamos a escala log no eixo x
yscale('log')
ylabel('população',fontsize=20)
legend(['recurso', 'consumidor'],fontsize=16)
savefig("diagrama_bifurcacao.png")


###### Forma Usual
figure(figsize=(8, 6)) 
tick_params(labelsize= 15)

def RM_season(y, t, r, alpha, T, K, a, h, e, d):
    # nesta função, o 't' aparece explicitamente
    return array([ y[0] * ( r * (1+alpha*sin(2*pi*t/T)) *
                           (1-y[0]/K) - a*y[1]/(1+a*h*y[0]) ),
    y[1] * (e*a*y[0]/(1+a*h*y[0]) - d) ])

t = arange(0, 2000, 1.)
y0 = [1., 1.]
pars =  (1., 0.1, 80., 10., 1., 0.1, 0.1, 0.1)
y = odeint(RM_season, y0, t, pars)
plot(t, y,linewidth=2.5)
xlabel('tempo',fontsize=20)
ylabel('população',fontsize=20)
legend(['recurso', 'consumidor'],fontsize=20)
savefig("pol.png")


# ressonancia
ymin = []
ymax = []
t = arange(0, 6000, 1.) # tempos
TT = arange(1, 80, 2) # períodos
for T in TT:
    pars =  (1., 0.1, T, 10., 1., 0.1, 0.1, 0.1)
    y = odeint(RM_season, y0, t, pars)
    ymin.append(y[-1000:,:].min(axis=0))
    ymax.append(y[-1000:,:].max(axis=0))
ymin = array(ymin)
ymax = array(ymax)

figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
plot(TT, ymin[:,0], 'g', label='recurso',lw=3.5)
plot(TT, ymin[:,1], 'b', label='consumidor',lw=3.5)
plot(TT, ymax[:,0], 'g',lw=3.5)
plot(TT, ymax[:,1], 'b',lw=3.5)
legend(loc='best')
yscale('log')
xlabel('$T$',fontsize=20)
ylabel('Populações min/max',fontsize=20)
legend(['recurso', 'consumidor'],fontsize=20)
savefig("ressonancia.png")