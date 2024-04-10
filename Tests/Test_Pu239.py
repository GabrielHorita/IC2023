import Eq22_Pu239 as Pu239
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x

energy_range = np.linspace(2., 8., 25)
print(" Spectrum:", Pu239 )
spectral_values = Pu239.Spectrum_Pu239(energy_range)
plt.plot(energy_range, spectral_values)
plt.xlabel('Energy')
plt.ylabel('Spectral Values')
plt.title('Neutrino Spectrum for Plutoniu 2399')
plt.show()

