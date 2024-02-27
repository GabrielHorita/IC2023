import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = []
y = []

with open("Graf7.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas[1:]:
        if not linha.startswith('#'):
            valores = linha.strip().split()
            if len(valores) == 2:
                x_original = float(valores[0])
                y_original = float(valores[1])

                x_adaptado = (x_original / 338) * 4
                y_adaptado = (y_original / 338) * 11 - 5

                x.append(x_adaptado)
                y.append(y_adaptado)

f = interp1d(x, y, kind='cubic')

def calcular_valor_de_y(valor_de_x):
    return f(valor_de_x)
def sigmacc(valor_de_x):
    return np.log10((10**4.0)*np.sqrt((valor_de_x +1)**2 -1)*(valor_de_x + 1))

x_smooth = np.linspace(min(x), max(x), 100)

y_smooth = f(x_smooth)

# O grafico é gerado pelas linhas abaixo
plt.scatter(x, y, label="Dados")
plt.plot(x_smooth, y_smooth, label="Curva", color='red')
valor_y_sigmacc = sigmacc(x_smooth)
plt.xlabel("Valores de X (0 a 4)")
plt.ylabel("Valores de Y (-5 a 6)")
plt.plot(x_smooth,valor_y_sigmacc, color='green')
plt.title("Graf7")
plt.grid(True)

plt.legend()

#Solicitando um valor para encontrar o seu correspondente no eixo Y, alterado e sem o ponto extra
valor_x_desejado = float(input("Digite um valor de X: "))


valor_y_correspondente = f(valor_x_desejado)


print(f"Para x = {valor_x_desejado}, y = {valor_y_correspondente}")



plt.legend()
plt.ylim([-5,6])
plt.show()
