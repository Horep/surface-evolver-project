import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
V_0 = r_U**3
angle = np.array([0, 30, 60, 89])

#plt.figure(figsize=(3, 4))
vol60 = 0.052*np.ones(4)
error60 = 0.0005/2*np.ones(4)
vol60 = vol60 + error60
plt.errorbar(angle, vol60/V_0, yerr=error60/V_0, xerr=None, label=r'$\theta_{YL} = 60\degree$')

vol75 = 0.0485*np.ones(4)
error75 = 0.0005/2*np.ones(4)
vol75 = vol75 + error75
plt.errorbar(angle, vol75/V_0, yerr=error75/V_0, xerr=None, label=r'$\theta_{YL} = 75\degree$')

vol90 = 0.047*np.ones(4)
error90 = 0.0005/2*np.ones(4)
vol90 = vol90 + error90
plt.errorbar(angle, vol90/V_0, yerr=error90/V_0, xerr=None, label=r'$\theta_{YL} = 90\degree$')

vol105 = 0.047*np.ones(4)
error105 = 0.0005/2*np.ones(4)
vol105 = vol105 + error105
plt.errorbar(angle, vol105/V_0, yerr=error105/V_0, xerr=None, label=r'$\theta_{YL} = 105\degree$')

vol120 = 0.049*np.ones(4)
error120 = 0.0005/2*np.ones(4)
vol120 = vol120 + error120
plt.errorbar(angle, vol120/V_0, yerr=error120/V_0, xerr=None, label=r'$\theta_{YL} = 120\degree$')

plt.ylabel(r"Min Volume $/ r_{U}^3$")
plt.xticks(np.arange(0, 95, 30), np.arange(0, 95, 30))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.legend(bbox_to_anchor=(1,1))
plt.savefig("varieddegreeminimumvolume.pdf", bbox_inches='tight', pad_inches=0.0)