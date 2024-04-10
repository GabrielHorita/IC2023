# -*- coding: utf-8 -*-
"""

@author: P.Chimenti, G.Horita
"""

import SessaodeChoque.Nu_CC as G9
import numpy as np
from matplotlib import pyplot as plt
import SessaodeChoque.Nu_CC as NUCC

def func(x):
    return x

print(" Testing Graf9... ")

print(" The crosssection is:", G9.calcular_valor_de_y( 2 ) )

print(" Testing Graf9... ")

xvals = np.arange(0.1, 8, 0.1)
yvals = NUCC.sigma_nucc(xvals)

plt.plot(xvals,yvals)
plt.show()