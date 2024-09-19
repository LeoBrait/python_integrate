# não precisamos fazer isso de novo: se a célula acima já foi executada,
# as bibliotecas já foram importadas, mas repetimos aqui por conveniência.
from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

t = arange(0, 50., 0.01)

# parâmetros
r = 2.
c = 0.5
e = 0.1
d = 1.

# condição inicial: este é um array agora!
x0 = array([1., 3.])

# a função ainda recebe apenas `x`, mas será um array, não um número
# em python, arrays são numerados de 0, então o primeiro elemento
# é x[0], o segundo é x[1]. Os colchetes `[ ]` definem um
# lista, que é convertida em um array usando a função `array()`.
# Observe que a primeira entrada corresponde a dV/dt e a segunda a dP/dt
def LV(x, t, r, c, e, d):
    return array([ r*x[0] - c * x[0] * x[1],
                   e * c * x[0] * x[1] - d * x[1] ])

# Agora, chamamos a função que faz a integração
# a ordem dos argumentos é a seguinte: a função derivada,
# a condição inicial, os pontos onde queremos a solução, e
# uma lista de parâmetros
x = odeint(LV, x0, t, (r, c, e, d))

# Agora `x` é um array de 2 dimensões de tamanho 5000 x 2 (5000 passos de tempo por 2
#variáveis). Podemos verificar assim:
print('shape of x:', x.shape)

# plotando as soluções
figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
plot(t, x,linewidth=2.5)
xlabel('t',fontsize=20) # definindo rótulo do eixo x
ylabel('populações',fontsize=20) # e do eixo y
legend(['V', 'P'], loc='upper right',fontsize=16)

# salvar a figura
savefig('test.png')

figure(figsize=(8, 6)) 
tick_params(labelsize= 15)
# `x[0,0]` é o primeiro valor (1ª linha, 1ª coluna), `x[0,1]` é o valor de
# a 1ª linha, 2ª coluna, que corresponde ao valor de P no tempo
# inicial. Traçamos apenas este ponto primeiro para saber onde começamos:
plot(x[0,0], x[0,1], 'o',markersize=10,zorder=3, color='blue')
print('Condições iniciais:', x[0])

# `x[0]` ou (equivalentemente) x[0,:] é a primeira linha e `x[:,0]` é a primeira
# coluna. Observe que os dois pontos `:` representam todos os valores desse eixo. Nós iremos
# plotar a segunda coluna (P) contra a primeira (V):
plot(x[:,0], x[:,1],linewidth=2.4)
xlabel('V',fontsize=20)
ylabel('P',fontsize=20)

# Vamos calcular e plotar outra solução com uma condição inicial diferente
x2 = odeint(LV, [10., 4.], t, (r, c, e, d))
plot(x2[:,0], x2[:,1],linewidth=2.5)
plot(x2[0,0], x2[0,1], 'o',markersize=10,color='red')

# salvar a figura
savefig('test2.png')