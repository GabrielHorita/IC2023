import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

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


valor_x_desejado = float(input("Digite um valor de X: "))


valor_y_correspondente = f(valor_x_desejado)


plt.scatter(x, y, label="Dados")
plt.plot(x_smooth, f(x_smooth), label="Linha", color='red')
valor_y_sigmacc = sigmacc(x_smooth)
plt.xlabel("Valores de X (0 a 3)")  # Origem em 0 e limite em 3
plt.ylabel("Valores de Y (-1 a 6)")  # Origem em -1 e máximo em 6
plt.plot(x_smooth,valor_y_sigmacc, color='green')
plt.title("Gráfico ds Linha com Ponto")
plt.grid(True)


print(f"Para x = {valor_x_desejado}, o valor correspondente de Y é {valor_y_correspondente}")

plt.legend()
plt.ylim([-1,6])
plt.xlim([0,3])
plt.show()
