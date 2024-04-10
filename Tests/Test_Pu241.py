import Eq22_Pu241 as Pu241
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x

energy_range = np.linspace(2., 8., 25)

print(" Spectrum:", Pu241 )
spectral_values = Pu241.Spectrum_Pu241(energy_range)
plt.plot(energy_range, spectral_values)
plt.xlabel('Energy')
plt.ylabel('Spectral Values')
plt.title('Neutrino Spectrum for Plutoniu 241')
plt.show()