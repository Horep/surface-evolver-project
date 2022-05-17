import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#plt.figure(figsize=(3, 5))
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain', useOffset=False)
r_U = 0.5
A = np.pi * r_U**2
angle=np.array([0, 15, 30, 45, 60, 75, 89])
angle = np.array(angle)
area = np.array([0.796391914837418,0.796392062914466,0.796392467208879,0.796393019449535,0.796393571697725,0.796393975912054,0.796394123292714])

sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T


sinm90, cosm90, c90 = np.linalg.lstsq(A1, area/A, rcond=None)[0]

mag90 = np.sqrt(cosm90**2 + sinm90**2)

phi90 = np.arctan2(sinm90/mag90, -cosm90/mag90)*180/np.pi
x1 = np.linspace(0, 90, 1000)
y1 = c90+ cosm90*np.cos(2*np.pi*x1/180) +sinm90 *np.sin(2*np.pi*x1/180)

plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.ylabel(r"Area$ /(\pi/4)$")

ax.plot(x1, y1, label=r"$ c + m_{c} \cos(2\vartheta) + m_{s} \sin(2\vartheta)$", color='orange')
ax.plot(angle, area/A, marker=".", linestyle='None', color='blue')

ax.legend(bbox_to_anchor=(0.7,1.13))
plt.savefig("LargeCylinderAreaChange.pdf", bbox_inches='tight', pad_inches=0.0)
