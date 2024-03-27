import numpy as np
import matplotlib.pyplot as plt
import os

file_dir = os.path.dirname(os.path.realpath(__file__))

print("Testing neutrino spectrum.")

spectral_coefficients_U = np.array([ 4.833e-1 , 1.927e-1 , -1.283e-1 , -6.762e-3 , 2.233e-3 , -1.536e-4 ])

print("Uranium 238 data:", spectral_coefficients_U)

def Spectrum_U_238( E ):
    """ This funtion implements the Huber-Muelle Model from arXiv:1101.2663, table 6 """
    exponent = 0
    for i in range(6):
        exponent += spectral_coefficients_U[i]*np.power(E,i)
    return np.exp(exponent)

energy_range = np.linspace( 2., 8., 25)

spectral_values = Spectrum_U_238(energy_range)


