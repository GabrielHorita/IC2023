import Eq22_U238 as U238
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return x

energy_range = np.linspace(2., 8., 25)
print(" Spectrum:", U238 )
spectral_values = U238.Spectrum_U_238(energy_range)
plt.plot(energy_range, spectral_values)
plt.xlabel('Energy')
plt.ylabel('Spectral Values')
plt.title('Neutrino Spectrum for Uranio 238')
plt.show()