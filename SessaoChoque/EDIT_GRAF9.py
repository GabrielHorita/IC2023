import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = []
y = []

with open("Graf9.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        if not linha.startswith('#'):
            valores = linha.strip().split()
            if len(valores) == 2:
                x_original = float(valores[0])
                y_original = float(valores[1])


                x_adaptado = (x_original / 338) * 3
                y_adaptado = (y_original / 338) * 9 + (-5)

                x.append(x_adaptado)
                y.append(y_adaptado)


f = interp1d(x, y, kind='cubic')


def calcular_valor_de_y(valor_de_x):
    return f(valor_de_x)

def sigmacc(valor_de_x):
    return np.log10((10**4.5)*np.sqrt((valor_de_x +1)**2 -1)*(valor_de_x + 1))

