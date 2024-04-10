# -*- coding: utf-8 -*-
"""

@author: P.Chimenti, G.Horita
"""

import SessaodeChoque.AntiNu_CN_QE as G7
import numpy as np
from matplotlib import pyplot as plt
import SessaodeChoque.AntiNu_CN_QE as ANCNQE

def func(x):
    return x

print(" Testing Graf7... ")

print(" The crosssection is:", G7.calcular_valor_de_y( 2) )

print(" Testing Graf7... ")

xvals = np.arange(0.1, 8, 0.1)
yvals = ANCNQE.sigma_ancnqe(xvals)

plt.plot(xvals,yvals)
plt.show()
