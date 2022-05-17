import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
#ax.ticklabel_format(style='plain', useOffset=False)
r_U = 0.5
A = np.pi * r_U**2

angle=np.array([0, 15, 30, 45, 60, 75, 89])
area80 = np.array([0.800531177191311,0.800531354016313,0.800531397075013,0.800532018077744,0.800532521985760,0.800533326828193,0.800533412362009])
area90 = np.array([0.796391914837418,0.796392062914466,0.796392467208879,0.796393019449535,0.796393571697725,0.796393975912054,0.796394123292714])
area100 = np.array([0.800891933692004,0.800892026279209,0.800892383218326,0.800892908846051,0.800893456195664,0.800893871034926,0.800894122436726])
sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T

sinm80, cosm80, c80 = np.linalg.lstsq(A1, area80/A, rcond=None)[0]
sinm90, cosm90, c90 = np.linalg.lstsq(A1, area90/A, rcond=None)[0]
sinm100, cosm100, c100 = np.linalg.lstsq(A1, area100/A, rcond=None)[0]

mag80 = np.sqrt(cosm80**2 + sinm80**2)
phi80 = np.arctan2(sinm80/mag80, -cosm80/mag80)*180/np.pi
mag90 = np.sqrt(cosm90**2 + sinm90**2)
phi90 = np.arctan2(sinm90/mag90, -cosm90/mag90)*180/np.pi
mag100 = np.sqrt(cosm100**2 + sinm100**2)
phi100 = np.arctan2(sinm100/mag100, -cosm100/mag100)*180/np.pi

x1 = np.linspace(0, 90, 1000)
y80 = sinm80*np.sin(2*np.pi*x1/180) + cosm80*np.cos(2*np.pi*x1/180)
y90 = sinm90*np.sin(2*np.pi*x1/180) + cosm90*np.cos(2*np.pi*x1/180)
y100 = sinm100*np.sin(2*np.pi*x1/180) + cosm100*np.cos(2*np.pi*x1/180)


plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.ylabel(r"(Area$ - \mathcal{A}(45\degree-\phi/2)) /\pi r_{U}^2$")

ax.plot(angle, area80/A - c80, marker=".", linestyle='None', label=r"$\theta_{YL} = 80\degree$", color='blue')
ax.plot(angle, area90/A - c90, marker=".", linestyle='None', label=r"$\theta_{YL} = 90\degree$", color='orange')
ax.plot(angle, area100/A - c100, marker=".", linestyle='None', label=r"$\theta_{YL} = 100\degree$", color='green')


ax.plot(x1,y80, label=r"NG $80\degree$", color='blue')
ax.plot(x1,y90, label=r"NG $90\degree$", color='orange')
ax.plot(x1,y100, label=r"NG $100\degree$", color='green')


plt.legend(bbox_to_anchor=(1.33,1.1))
plt.savefig("LargeCylinderAreaChangeVaried.pdf", bbox_inches='tight', pad_inches=0.0)
