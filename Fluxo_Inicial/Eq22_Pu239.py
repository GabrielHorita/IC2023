import numpy as np
import matplotlib.pyplot as plt


print("Testing neutrino spectrum.")

spectral_coefficients_Pu239 = np.array([ 6.413 , -7.432 , 3.535 , -8.820e-1 , 1.025e-1 , -4.550e-3  ])

print("Plutonium 239 data:", spectral_coefficients_Pu239)

def Spectrum_Pu239( E ):
    """ This funtion implements the Huber-Muelle Model from arXiv:1101.2663, table 6 """
    exponent = 0
    for i in range(6):
        exponent += spectral_coefficients_Pu239[i]*np.power(E,i)
    return np.exp(exponent)

energy_range = np.linspace( 2., 8., 25)

spectral_values = Spectrum_Pu239(energy_range)

