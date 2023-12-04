import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = []
y = []


with open("Graf5.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        valores = linha.strip().split()
        if len(valores) == 2:
            x_original = float(valores[0])
            y_original = float(valores[1])


            x_adaptado = (x_original / 338) * 8
            y_adaptado = (y_original / 338) * (7 - 4) + 4

            x.append(x_adaptado)
            y.append(y_adaptado)


f = interp1d(x, y, kind='cubic')

fi = (1e10)/202e6

def calcular_valor_de_y(valor_de_x):
    return f(valor_de_x)

def RS(E):
    fi = (1e9) / 202e6


valor_x_input = float(input("Digite um valor de X: "))


valor_y_output = calcular_valor_de_y(valor_x_input)


print(f"Para X = {valor_x_input}, Y = {valor_y_output}")

valor_y_output = calcular_valor_de_y(valor_x_input)

valor_y_output = calcular_valor_de_y(valor_x_input)

Ultimo_resultado = valor_y_output * ((1 / (4 * 3.14 * 900))*(1e9/202e6))/1.13



print("Resultado final = ",{Ultimo_resultado})



