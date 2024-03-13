import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, "Graf8p.txt")

print(file_path)

x = []
y = []

with open("Graf8p.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        if not linha.startswith('#'):
            valores = linha.strip().split()
            if len(valores) == 2:
                x_original = float(valores[0])
                y_original = float(valores[1])

                x_adaptado = (x_original / 338) * 3
                y_adaptado = (y_original / 338) * 7 - 1

                x.append(x_adaptado)
                y.append(y_adaptado)

x_smooth = np.linspace(min(x), max(x), 100)

f = interp1d(x, y, kind='cubic')
def calcular_valor_de_y(valor_de_x):
    return f(valor_de_x)

def sigmacc(valor_de_x):
    return np.log10((10**1.0)*np.sqrt((valor_de_x +1)**2 -1)*(valor_de_x + 1))

