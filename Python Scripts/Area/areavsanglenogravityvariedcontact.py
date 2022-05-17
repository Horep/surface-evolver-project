import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain', useOffset=False)
r_U = 0.5
A = np.pi * r_U**2

angle=np.array([0, 15, 30, 45, 60, 75, 89])
area80g = np.array([63.8811998980939,63.8812601557727,63.8813960275309,63.8815096395522,63.8815396319041,63.8815094774670,63.8814879026516])
area90g = np.array([63.8770597832058,63.8771004245160,63.8771979686871,63.8772941597390,63.8773446062667,63.8773542164548,63.8773527427839])
area100g = np.array([63.8805468460943,63.8805563984148,63.8805940441690,63.8806589977368,63.8807321747722,63.8807940387861,63.8808198542472])
area80 = np.array([63.8802440313871,63.8802626040884,63.8803137008116,63.8803830808285,63.8804520482593,63.8805025357315,63.8805209733438])
area90 = np.array([63.8765234696375,63.8765428758136,63.8765957439084,63.8766676079954,63.8767390669129,63.8767911221136,63.8768100350073])
area100 = np.array([63.8806533606093,63.8806719102597,63.8807230032653,63.8807927230334,63.8808621230924,63.8809126394716,63.8809309826305])
crction = 63.025661810242400*np.ones(7)
area80g = area80g - crction
area90g = area90g - crction
area100g = area100g - crction
area80 = area80 - crction
area90 = area90 - crction
area100 = area100 - crction
sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T

sinm80g, cosm80g, c80g = np.linalg.lstsq(A1, area80g/A, rcond=None)[0]
sinm100g, cosm100g, c100g = np.linalg.lstsq(A1, area100g/A, rcond=None)[0]

sinm90g, cosm90g, c90g = np.linalg.lstsq(A1, area90g/A, rcond=None)[0]
mag90g = np.sqrt(cosm90g**2 + sinm90g**2)
phi90g = np.arctan2(sinm90g/mag90g, -cosm90g/mag90g)*180/np.pi

mag80g = np.sqrt(cosm80g**2 + sinm80g**2)
phi80g = np.arctan2(sinm80g/mag80g, -cosm80g/mag80g)*180/np.pi

mag100g = np.sqrt(cosm100g**2 + sinm100g**2)
phi100g = np.arctan2(sinm100g/mag100g, -cosm100g/mag100g)*180/np.pi

sinm80, cosm80, c80 = np.linalg.lstsq(A1, area80/A, rcond=None)[0]
sinm90, cosm90, c90 = np.linalg.lstsq(A1, area90/A, rcond=None)[0]
sinm100, cosm100, c100 = np.linalg.lstsq(A1, area100/A, rcond=None)[0]


mag80 = np.sqrt(cosm80**2 + sinm80**2)
phi80 = np.arctan2(sinm80/mag80, -cosm80/mag80)*180/np.pi

mag100 = np.sqrt(cosm100**2 + sinm100**2)

phi100 = np.arctan2(sinm100/mag100, -cosm100/mag100)*180/np.pi

x1 = np.linspace(0, 90, 1000)
y80 = sinm80*np.sin(2*np.pi*x1/180) + cosm80*np.cos(2*np.pi*x1/180)
y90 = sinm90*np.sin(2*np.pi*x1/180) + cosm90*np.cos(2*np.pi*x1/180)
y100 = sinm100*np.sin(2*np.pi*x1/180) + cosm100*np.cos(2*np.pi*x1/180)



y80g = sinm80g*np.sin(2*np.pi*x1/180) + cosm80g*np.cos(2*np.pi*x1/180)
y90g = sinm90g*np.sin(2*np.pi*x1/180) + cosm90g*np.cos(2*np.pi*x1/180)
y100g = sinm100g*np.sin(2*np.pi*x1/180) + cosm100g*np.cos(2*np.pi*x1/180)

plt.xticks(np.arange(0, 95, 10), np.arange(0, 95, 10))
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.ylabel(r"(Area$ - \mathcal{A}(45\degree-\phi/2)) /\pi r_{U}^2$")

plt.plot(angle, area90/A - c90, marker=".", linestyle='None', label=r"$\theta_{YL} = 90\degree$", color='orange')
plt.plot(angle, area80/A - c80, marker=".", linestyle='None', label=r"$\theta_{YL} = 80\degree$", color='blue')
plt.plot(angle, area100/A - c100, marker=".", linestyle='None', label=r"$\theta_{YL} = 100\degree$", color='green')


plt.plot(x1,y80, label=r"NG $80\degree$", color='blue')
plt.plot(x1,y90, label=r"NG $90\degree$", color='orange')
plt.plot(x1,y100, label=r"NG $100\degree$", color='green')


plt.legend(bbox_to_anchor=(1.33,1.1))
plt.savefig("NoGravCombinedAreaChange.pdf", bbox_inches='tight', pad_inches=0.0)
