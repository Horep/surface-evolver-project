import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
V_0 = r_U**3

#plt.figure(figsize=(3, 4))
density = np.array([1, 2, 3, 4, 5])/4

minvol = np.array([0.047, 0.054, 0.0605, 0.067, 0.074])
minvolerror = np.array([0.0005, 0.0005, 0.0005, 0.0005, 0.0005])/2
minvol += minvolerror

plt.errorbar(density, minvol/V_0, yerr=minvolerror/V_0, xerr=None, label=r'$V_{min}$')


A = np.vstack([density, np.ones(len(density))]).T
b, c = np.linalg.lstsq(A, minvol/V_0, rcond=None)[0]

x = np.linspace(1/4, 5/4, 1000)

#plt.plot(x, b*x + c, label=r"$a\theta_{YL}^2 + b\theta_{YL} + c$")

plt.legend()

plt.ylabel(r"Min Volume $/ r_{U}^3$")
plt.xticks(np.arange(1, 5+1, 1)/4, np.arange(1, 5+1, 1)/4)
plt.xlabel(r"Bond Number")
plt.legend(bbox_to_anchor=(1,1))
plt.savefig("MinVolVsDensity.pdf", bbox_inches='tight', pad_inches=0.0)