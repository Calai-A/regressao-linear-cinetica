from scipy.stats import linregress
import sys
from matplotlib import pyplot as plt
import math as math
import numpy as np


def plot_graph0 (lt,lc,nome_eixox,nome_eixoy):
    stats0 = linregress(lt,lc)
    plt.plot(lt, lc, label='original data')
    plt.legend()
    return plt.show()


def plot_graph1 (lt, lc, nome_eixox, nome_eixoy):
    for i in range(len(lc)):
        try:
            lc1.append(np.log(lc[i]))
        except:
            lc1.append(lc[i])

    lt1 = lt
    plt.plot(lt1, lc1,label='Plot dos dados linearizam para uma reação de ordem 1', color='b')
    plt.xlabel(nome_eixox, fontsize=13)
    plt.ylabel(nome_eixoy, fontsize=13)
    return plt.show()


def plot_graph2 (lt, lc, nome_eixox, nome_eixoy):
    lc2=[]
    lt2 = np.asarray(lt)
    for i in range(len(lc)):
        lc2.append(1 / lc[i])
    lc2 = np.asarray(lc2)
    plt.plot(lt2, lc2, label='Plot dos dados linearizam para uma reação de ordem 2', color='b')
    plt.xlabel(nome_eixox, fontsize=13)
    plt.ylabel(nome_eixoy, fontsize=13)
    return plt.show()

def abs_to_conc(lc,c0):
    lc.pop
    abs_conc = []
    for i in range(1,(len(lc)-1)):
        abs_conc.append(lc[-1] - lc[i])
    return abs_conc


def reg_lin0 (lt,lc):
    stats0 = linregress(lt,lc)
    r = (stats0[2])**2
    r= abs(r)
    if r >= 0.97:
        return print('\nA equação pode ser linearizada para uma reação de pseudordem 0\n'), print('Os dados da reta são:\n',stats0), lc
    else:
        return print('\nA equação não pode ser linearizada para uma reação de pseudordem 0')


def reg_lin1 (lt,lc):
    lc1 =[]
    lt1 =[]
    for i in range(len(lc)):
        try:
            lc1.append(np.log(lc[i]))
        except:
            lc1.append(12736173712)
        lt1.append(lt[i])
    stats1 = linregress(lt1,lc1)
    r = stats1[2]**2
    r = abs(r)
    if r >= 0.97:
        return print('\nA equação pode ser linearizada para uma reação de pseudordem 1\n'), print('Os dados da reta são:\n',stats1)
    else:
        return print('\nA equação não pode ser linearizada para uma reação de pseudordem 1')

def reg_lin2 (lt,lc):
    lc2=[]
    for i in range(len(lc)):
        try:
            lc2.append(1/lc[i])
        except ZeroDivisionError:
            lc2.append(231231231231)
    stats2 = linregress(lt,lc2)
    r = stats2[2]**2
    r = abs(r)
    if r >= 0.97:
        return print('\nA equação pode ser linearizada para uma reação de pseudordem 2\n'), print('Os dados da reta são:\n',stats2)
    else:
        return print('\nA equação não pode ser linearizada para uma reação de pseudordem 2')

print('================\t\nREGRESSÃO LINEAR\t\n================'
      '\n== Pseudo velocidades de reação ==\n')

while True:
    try:
        arg1 = sys.argv[1]
    except IndexError:
        arg1 = input('\n==\tDigite o nome do arquivo para análise\t==\nDigite "sair" para sair\t\n')
    if str.lower(arg1) == ('sair'):
        print('Você saiu do programa')
        exit()
    else:
        try:
            ler_arquivo = open(arg1,'r')
            print('Lendo o arquivo')
            teste = ler_arquivo.readlines()
            teste[0] = teste[0].split(' ')
            print('A leitura das linhas resultou nos seguintes dados: ',teste)
            if (teste[0][0]) == 'concentracao' or 'condutividade' or 'abs' or 'generico':
                break
            else:
                print('\n==\tERRO\t==\nEste arquivo NÃO é compatível com a formatação esperada\n')
        except:
            print('\n==\tERRO\t==\nEste arquivo não foi encontrado. Tente um nome válido\n')

a = open(arg1,'r')
l1 = a.readlines()
for i in range(len(l1)):
    l1[i] = l1[i].strip()
    l1[i] = l1[i].split(" ")
lc=[]
lt=[]
lc1=[]
lt1=[]
lc2=[]


for i in range(0, len(l1)):
    try:
        lc.append(float(l1[i][0]))
        lt.append(float(l1[i][1]))
    except:
        lc.append(str.lower(l1[i][0]))
        lt.append(str.lower(l1[i][1]))

print('Os dados recebidos do arquivo são', lc)
print('Os dados recebidos do arquivo são',lt)


if (lc[0]) == 'condutividade':
    lt.pop()
    print('================\nCálculo da velocidade a partir da condutividade\n================')
    Am = float(input('Insira o valor da condutividade iônica molar do sistema - valores em (uS. L) / (m.mol)'))
    lc = cond_to_conc(lc,Am)

if (lc[0]) == 'abs':
    lt.pop(0)
    lc.pop(0)
    abs_conc=[]
    print('====================================================\nCálculo da velocidade a partir de espectrofotometria\n====================================================')
    c0 = float(input('Determine a concentração inicial do reagente'))
    lc = abs_to_conc(lc,c0)
    lt.pop(0)
    lt.pop(-1)

if (lc[0]) == 'concentracao':
    lc.pop(0)
    lt.pop(0)

if (lc[0]) == 'generico':
    lc.pop(0)
    lt.pop(0)

print('Os dados de y são', lc)
print('Os dados de tempo são',lt)
print('\n== A análise dos dados mostra que == ')
reg_lin0(lt,lc)
reg_lin1(lt,lc)
reg_lin2(lt,lc)

while True:
    try:
        plote = input(('\nEscolha a operação para plotar o gráfico:\n\t1. Gŕafico linearizado para ordem 0\n\t2. Gráfico linearizado para ordem 1\n\t3. Gráfico linearizado para ordem 2\n\t4. Sair'))

        if plote == '1':
            nome_eixox = input('Unidades de X')
            nome_eixoy = input('Unidades de Y')
            plot_graph0(lt, lc, nome_eixox, nome_eixoy)

        elif plote == '2':
            nome_eixox = input('Unidades de X')
            nome_eixoy = input('Unidades de Y')
            plot_graph1(lt, lc, nome_eixox, nome_eixoy)


        elif plote == '3':
            nome_eixox = input('Unidades de X')
            nome_eixoy = input('Unidades de Y')
            plot_graph2(lt, lc, nome_eixox, nome_eixoy)
        if plote == '4':
            exit()

    except ValueError:
        print('Valor inválido, escolha apenas um dos três! sair para sair')

