import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
A = np.pi * r_U**2
angle = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,89]
angle = np.array(angle)
energy = np.array([12.7387967752096,12.7387981817180,12.7388020231163,12.7388082337107,12.7388165796922,12.7388268130270,12.7388386364068,12.7388516866491,12.7388655482968,12.7388798140723,12.7388940667112,12.7389079688996,12.7389209881098,12.7389327269852,12.7389428378005,12.7389510214100,12.7389570321952,12.7389606884647,12.7389618382452])


sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T


sinm90, cosm90, c90 = np.linalg.lstsq(A1, energy/A, rcond=None)[0]

x1 = np.linspace(0, 90, 1000)
y1 = c90+ cosm90*np.cos(2*np.pi*x1/180) +sinm90 *np.sin(2*np.pi*x1/180)

plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Angle $(\vartheta\degree)$")
plt.ylabel(r"Energy$ /\pi r_{U}^2 \sigma$")

plt.plot(angle, energy/A, marker=".", linestyle='None')
plt.plot(x1, y1, label=r"$ c + m_{c} \cos(2\vartheta) + m_{s} \sin(2\vartheta)$")

plt.legend()
plt.savefig("WithGravAngleChange1.pdf", bbox_inches='tight', pad_inches=0.0)
