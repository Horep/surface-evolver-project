import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
V_0 = r_U**3
contactangle = np.array([60, 75, 90, 105, 120])

minvol = np.array([0.065, 0.0615, 0.061, 0.064, 0.0715])
minvolerror = np.array([0.0005, 0.0005, 0.0005, 0.0005, 0.0005])

plt.errorbar(contactangle, minvol/V_0, yerr=minvolerror/V_0, xerr=None, label=r'$V_{min}$')


A = np.vstack([contactangle**2, contactangle, np.ones(len(contactangle))]).T
a, b, c = np.linalg.lstsq(A, minvol/V_0, rcond=None)[0]

x = np.linspace(60, 120, 1000)

plt.plot(x, a*x*x + b*x + c, label=r"$a\theta_{YL}^2 + b\theta_{YL} + c$")

plt.legend()

plt.ylabel(r"Min Volume $/ r_{U}^3$")
plt.xticks(np.arange(60, 125, 15), np.arange(60, 125, 15))
plt.xlabel(r"Contact Angle $(\theta_{YL}\degree)$")
plt.legend()
plt.savefig("minvolvscontactangle.pdf", bbox_inches='tight', pad_inches=0.0)