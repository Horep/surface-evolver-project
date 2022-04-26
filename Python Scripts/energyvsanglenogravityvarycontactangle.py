import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
A = np.pi * r_U**2

angle=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,89])
energy80 = np.array([0.901119829487668,0.900749544645552,0.899640115630796,0.897796887956737,0.895232068795967,0.891969152342168,0.888048136987216,0.883531570867048,0.878507988694120,0.873095868217133,0.867444169134288,0.861730231449614,0.856154301428788,0.850930753078419,0.846277384484072,0.842401567137449,0.839486985687017,0.837677980849393,0.837088901117050])
energy90 = np.array([0.850863098587774,0.850865300625838,0.850871836569172,0.850882501716674,0.850896962179316,0.850914766226555,0.850935360461251,0.850958107026657,0.850982304941028,0.851007212684749,0.851032072120493,0.851056129979945,0.851078661591899,0.851098992225457,0.851116515957298,0.851130712836301,0.851141163147408,0.851147558962652,0.851149625712924])
energy100 = np.array([0.793796661571946,0.794240508169187,0.795547832479884,0.797648059671085,0.800430443123646,0.803753452248207,0.807456223032301,0.811370694362484,0.815333973345518,0.819197526529800,0.822835107291836,0.826147414565963,0.829063894281390,0.831540815943575,0.833555836413788,0.835104637948764,0.836196308190201,0.836846077714704,0.837055098571961])

sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T

sinm80, cosm80, c80 = np.linalg.lstsq(A1, energy80/A, rcond=None)[0]
sinm100, cosm100, c100 = np.linalg.lstsq(A1, energy100/A, rcond=None)[0]

x1 = np.linspace(0, 90, 1000)
y80 = sinm80*np.sin(2*np.pi*x1/180) + cosm80*np.cos(2*np.pi*x1/180)+c80
y100 = sinm100*np.sin(2*np.pi*x1/180) + cosm100*np.cos(2*np.pi*x1/180)+c100

plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.ylabel(r"Energy$ /\pi r_{U}^2 \sigma$")
plt.plot(angle, energy90/A, marker=".", linestyle='None', label=r"$\theta_{YL} = 90\degree$")
plt.plot(angle, energy80/A, marker=".", linestyle='None', label=r"$\theta_{YL} = 80\degree$")
plt.plot(angle, energy100/A, marker=".", linestyle='None', label=r"$\theta_{YL} = 100\degree$")


plt.plot(x1,y80, label=r"Lst Sqr $80\degree$")
plt.plot(x1,y100, label=r"Lst Sqr $100\degree$")
plt.legend()
plt.savefig("NoGravAngleChangeVariedContactV1.pdf", bbox_inches='tight', pad_inches=0.0)