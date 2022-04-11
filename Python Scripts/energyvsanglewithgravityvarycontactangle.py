import numpy as np
import matplotlib.pyplot as plt

r_U = 0.5
A = np.pi * r_U**2

angle=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,89])
energy80 = np.array([12.7857386562047,12.7854916478302,12.7847480634807,12.7835034441220,12.7817539675057,12.7795013728246,12.7767588867548,12.7735574133798,12.7699503147375,12.7660176631902,12.7618668774439,12.7576313817213,12.7534657911996,12.7495393952671,12.7460252530513,12.7430885032804,12.7408747444653,12.7394979075872,12.7390493927875])
energy90 = np.array([12.7387967752096,12.7387981817180,12.7388020231163,12.7388082337107,12.7388165796922,12.7388268130270,12.7388386364068,12.7388516866491,12.7388655482968,12.7388798140723,12.7388940667112,12.7389079688996,12.7389209881098,12.7389327269852,12.7389428378005,12.7389510214100,12.7389570321952,12.7389606884647,12.7389618382452])
energy100 = np.array([12.6847040220676,12.6850143499996,12.6859255169447,12.6873807044948,12.6892911341595,12.6915438661237,12.6940108066504,12.6965594941765,12.6990732437558,12.7014415582094,12.7035808922532,12.7054378166343,12.7069751113995,12.7081852654912,12.7091217738804,12.7097245077357,12.7098670367166,12.7102220468837,12.7102669321970])

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
plt.savefig("WithGravAngleChangeVariedContactV1.pdf", bbox_inches='tight', pad_inches=0.0)