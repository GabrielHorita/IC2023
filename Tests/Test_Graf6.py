# -*- coding: utf-8 -*-
"""

@author: P.Chimenti, G.Horita
"""

import SessaodeChoque.AntiNu_CC_INE as G
import numpy as np
from matplotlib import pyplot as plt
import SessaodeChoque.AntiNu_CC_INE as ANCCINE

def func(x):
    return x

print(" Testing Graf6... ")

print(" The crosssection is:", G.calcular_valor_de_y( 2 ) )

print(" Testing Graf6... ")

xvals = np.arange(0.1, 8, 0.1)
yvals = ANCCINE.sigma_anccine(xvals)

plt.plot(xvals,yvals)
plt.show()