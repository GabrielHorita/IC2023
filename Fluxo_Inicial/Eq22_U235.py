import numpy as np
import matplotlib.pyplot as plt
import os

file_dir = os.path.dirname(os.path.realpath(__file__))

print("Testing neutrino spectrum.")

spectral_coefficients_U = np.array([ 3.217, -3.111, 1.395, -3.690e-1, 4.445e-2, -2.053e-3])

print("Uranium 235 data:", spectral_coefficients_U)

def Spectrum_U_235( E ):
    """ This funtion implements the Huber-Muelle Model from arXiv:1101.2663, table 6 """
    exponent = 0
    for i in range(6):
        exponent += spectral_coefficients_U[i]*np.power(E,i)
    return np.exp(exponent)

energy_range = np.linspace( 2., 8., 25)

spectral_values = Spectrum_U_235(energy_range)

