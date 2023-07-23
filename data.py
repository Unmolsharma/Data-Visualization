import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'



unemploymentrate = []
immigrants = []

i = 1
while i < 9:
    unemploymentrate.append(i)
    i+=1

i = 3
while i < 11:
    immigrants.append(i)
    i += 1

plt.plot(unemploymentrate,immigrants)
plt.xlabel ('X Coordinate')
plt.title ('My project')
plt.show()

mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
