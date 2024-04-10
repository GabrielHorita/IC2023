import Eq22_U235 as U235
import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return x

energy_range = np.linspace(2., 8., 25)
print(" Spectrum:", U235 )

spectral_values = U235.Spectrum_U_235(energy_range)
plt.plot(energy_range, spectral_values)
plt.xlabel('Energy')
plt.ylabel('Spectral Values')
plt.title('Neutrino Spectrum for Uranio 235')
plt.show()