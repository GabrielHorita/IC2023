# -*- coding: utf-8 -*-
"""

@author: P.Chimenti, G.Horita
"""

import SessaodeChoque.AntiNu_CC_QE as G5
import numpy as np
from matplotlib import pyplot as plt

def func(x):
    return x

print(" Testing Graf5... ")

print(" The crosssection is:", G5.calcular_valor_de_y( 2 ) )

print(" Testing Graf5... ")

xvals = np.arange(0.1, 8, 0.1)
yvals = G5.sigma_anccqe(xvals)

plt.plot(xvals,yvals)
plt.show()