import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
A = np.pi * r_U**2
angle = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,89]
angle = np.array(angle)
energy = np.array([0.850863098587774,0.850865300625838,0.850871836569172,0.850882501716674,0.850896962179316,0.850914766226555,0.850935360461251,0.850958107026657,0.850982304941028,0.851007212684749,0.851032072120493,0.851056129979945,0.851078661591899,0.851098992225457,0.851116515957298,0.851130712836301,0.851141163147408,0.851147558962652,0.851149625712924])

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
plt.savefig("NoGravAngleChange1.pdf", bbox_inches='tight', pad_inches=0.0)
