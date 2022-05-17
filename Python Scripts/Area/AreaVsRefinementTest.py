import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain', useOffset=False)
r_U = 0.5
A = np.pi * r_U**2

refinement = np.array([0, 1, 2, 3])
measuredarea = np.array([0.850857827226400, 0.850862682415682, 0.850863045973359, 0.850863093569686])
plt.xticks(refinement,refinement)
plt.ylabel("Liquid-air Surface Area")
plt.xlabel("Additional Refinements")
ax.plot(refinement, measuredarea/A,linestyle='--',marker='o')

plt.savefig("areavsrefinementtest.pdf", bbox_inches='tight', pad_inches=0.0)
