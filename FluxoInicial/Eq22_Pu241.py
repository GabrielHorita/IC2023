import numpy as np
import matplotlib.pyplot as plt


print("Testing neutrino spectrum.")

spectral_coefficients_Pu241 = np.array([ 3.251 , -3.024 , 1.428 , -3.675e-1 , 4.253e-2 , -1.896e-3 ])

print("Plutonium 241 data:", spectral_coefficients_Pu241)

def Spectrum_Pu241( E ):
    """ This funtion implements the Huber-Muelle Model from arXiv:1101.2663, table 6 """
    exponent = 0
    for i in range(6):
        exponent += spectral_coefficients_Pu241[i]*np.power(E,i)
    return np.exp(exponent)

energy_range = np.linspace( 2., 8., 25)

spectral_values = Spectrum_Pu241(energy_range)

print(spectral_values)

plt.plot(energy_range,spectral_values)
plt.yscale("log")
plt.show()
