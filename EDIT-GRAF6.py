import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = []
y = []

with open("Graf6.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        if not linha.startswith('#'):
            valores = linha.strip().split()
            if len(valores) == 2:
                x_original = float(valores[0])
                y_original = float(valores[1])

                x_adaptado = (x_original / 338) * 12
                y_adaptado = (y_original / 338) * (7 - 3) + 3

                x.append(x_adaptado)
                y.append(y_adaptado)


f = interp1d(x, y, kind='cubic')


def calcular_valor_de_y(valor_de_x):
    return f(valor_de_x)
#Eq da funcao
def sigmacc(valor_de_x):
    return np.log10((10**4.2)*np.sqrt((valor_de_x +1)**2 -1)*(valor_de_x + 1))

valor_x_input = float(input("Digite um valor de X: "))


valor_y_output = calcular_valor_de_y(valor_x_input)


print(f"Para X = {valor_x_input}, Y = {valor_y_output}")


x_smooth = np.linspace(min(x), max(x), 100)
y_smooth = f(x_smooth)
valor_y_sigmacc = sigmacc(x_smooth)
plt.scatter(x, y, label="Dados")
plt.plot(x_smooth, y_smooth, label="Curva Suave", color='red')
plt.plot(x_smooth,valor_y_sigmacc, color='green')
plt.xlabel("Valores de X (0 a 12)")
plt.ylabel("Valores de Y (3 a 7)")
plt.title("Gráfico de Dispersão com Curva Suave")
plt.grid(True)
plt.ylim([3, 7])
plt.xlim([0,12])
plt.legend()
plt.show()
