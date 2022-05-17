import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.ticklabel_format(style='plain', useOffset=False)
r_U = 0.5
A = np.pi * r_U**2
area80g = np.genfromtxt('80_degree_with_gravity_area.csv', delimiter=',')
angle = np.genfromtxt('angles.csv', delimiter=',')
area80grev = np.genfromtxt('80_degree_with_gravity_area_reverse.csv', delimiter=',')
anglerev = np.genfromtxt('anglesrev.csv', delimiter=',')
sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T

sinm80g, cosm80g, c80g = np.linalg.lstsq(A1, area80g/A, rcond=None)[0]

x1 = np.linspace(0, 90, 1000)
y80g = c80g + sinm80g*np.sin(2*np.pi*x1/180) + cosm80g*np.cos(2*np.pi*x1/180)

plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.ylabel(r"(Area$/\pi r_{U}^2$")

plt.plot(angle, area80g/A, marker=".", linestyle='None', label=r"$0\degree$ initial", color='blue')
plt.plot(anglerev, area80grev/A, marker=".", linestyle='None', label=r"$89\degree$ initial", color='orange')
#plt.plot(x1, y80g, label=r"G $80\degree$", color='blue', linestyle='dashed')
plt.legend()
plt.savefig("80degreemorepointsarea.pdf", bbox_inches='tight', pad_inches=0.0)