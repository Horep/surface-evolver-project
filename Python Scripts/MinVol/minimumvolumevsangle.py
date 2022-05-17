import numpy as np
import matplotlib.pyplot as plt

angle = np.array([0, 30, 60, 89])
vol = np.array([0.0613828125, 0.0613671875, 0.0614453125, 0.06140625])
error = np.array([0.0000078125, 0.0000390625, 0.0000390625, 0.00015625])


plt.errorbar(angle, vol, yerr=error, xerr=None, fmt='none')
plt.ylabel(r"Min Volume")
plt.xticks(np.arange(0, 95, 30), np.arange(0, 95, 30))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.savefig("90degreeminimumvolume.pdf", bbox_inches='tight', pad_inches=0.0)
