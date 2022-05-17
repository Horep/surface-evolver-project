import matplotlib.pyplot as plt
import numpy as np
def magphase(sinm,cosm):
    mag = np.sqrt(sinm**2 + cosm**2)
    phi = np.arctan2(sinm/mag, -cosm/mag)*180/np.pi
    return mag, phi


r_U = 0.5
rinv = 1/r_U

angle = np.array([0, 15, 30, 45, 60, 75, 89])
lower80 = rinv*np.array([0.496846223623357,0.496897076012737,0.496803015820278,0.496156726448476,0.494894972843156,0.493556726393311,0.492975827144551])
upper80 = rinv*np.array([0.455554632219788,0.452997682236272,0.448921933991356,0.446522793028445,0.446718232547225,0.449347714906706,0.451203884755881])

lower90 = rinv*np.array([0.531901592794667,0.531957204208543,0.531836829235028,0.531038643269432,0.529493313602457,0.527858585138676,0.527150453387627])
upper90 = rinv*np.array([0.489436153661044,0.486558345910561,0.481686571098061,0.478625735049728,0.478927066898116,0.481929103700076,0.483967292544033])

lower100 = rinv*np.array([0.567332081925342,0.567418121607390,0.567318974600174,0.566403290972710,0.564568072626077,0.562602589057438,0.561746011520796])
upper100 = rinv*np.array([0.522690756730912,0.519451591987126,0.513597818903230,0.509695388756183,0.510308640187366,0.513920180608159,0.516190598061241])

sinx = np.sin(2*angle*np.pi/180)
cosx = np.cos(2*angle*np.pi/180)
A1 = np.vstack([sinx, cosx, np.ones(len(sinx))]).T

sinm80L, cosm80L, c80L = np.linalg.lstsq(A1, lower80, rcond=None)[0]
mag80L, phi80L = magphase(sinm80L,cosm80L)
sinm90L, cosm90L, c90L = np.linalg.lstsq(A1, lower90, rcond=None)[0]
mag90L, phi90L = magphase(sinm90L,cosm90L)
sinm100L, cosm100L, c100L = np.linalg.lstsq(A1, lower100, rcond=None)[0]
mag100L, phi100L = magphase(sinm100L,cosm100L)

sinm80U, cosm80U, c80U = np.linalg.lstsq(A1, upper80, rcond=None)[0]
mag80U, phi80U = magphase(sinm80U,cosm80U)
sinm90U, cosm90U, c90U = np.linalg.lstsq(A1, upper90, rcond=None)[0]
mag90U, phi90U = magphase(sinm90U,cosm90U)
sinm100U, cosm100U, c100U = np.linalg.lstsq(A1, upper100, rcond=None)[0]
mag100U, phi100U = magphase(sinm100U,cosm100U)

x1 = np.linspace(0, 90, 1000)
y80L = c80L + sinm80L*np.sin(2*np.pi*x1/180) + cosm80L*np.cos(2*np.pi*x1/180)
y90L = c90L + sinm90L*np.sin(2*np.pi*x1/180) + cosm90L*np.cos(2*np.pi*x1/180)
y100L = c100L + sinm100L*np.sin(2*np.pi*x1/180) + cosm100L*np.cos(2*np.pi*x1/180)
y80U = c80U + sinm80U*np.sin(2*np.pi*x1/180) + cosm80U*np.cos(2*np.pi*x1/180)
y90U = c90U + sinm90U*np.sin(2*np.pi*x1/180) + cosm90U*np.cos(2*np.pi*x1/180)
y100U = c100U + sinm100U*np.sin(2*np.pi*x1/180) + cosm100U*np.cos(2*np.pi*x1/180)

plt.plot(x1,y80L, linestyle='--', color='blue')
plt.plot(x1,y90L, linestyle='--', color='orange')
plt.plot(x1,y100L, linestyle='--', color='green')
plt.plot(x1,y80U, linestyle='--', color='blue')
plt.plot(x1,y90U, linestyle='--', color='orange')
plt.plot(x1,y100U, linestyle='--', color='green')


#plt.plot(angle,lower80)
#plt.plot(angle,lower90)
#plt.plot(angle,lower100)

plt.plot(angle, lower80, marker="v", linestyle='None', label=r"$\theta_{YL} = 80\degree$ L", color='blue')
plt.plot(angle, lower90, marker="v", linestyle='None', label=r"$\theta_{YL} = 90\degree$ L", color='orange')
plt.plot(angle, lower100, marker="v", linestyle='None', label=r"$\theta_{YL} = 100\degree$ L", color='green')

plt.plot(angle, upper80, marker="^", linestyle='None', label=r"$\theta_{YL} = 80\degree$ U", color='blue')
plt.plot(angle, upper90, marker="^", linestyle='None', label=r"$\theta_{YL} = 90\degree$ U", color='orange')
plt.plot(angle, upper100, marker="^", linestyle='None', label=r"$\theta_{YL} = 100\degree$ U", color='green')

plt.ylabel(r"Width/$r_{U}$")
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.legend(bbox_to_anchor=(1,1))
plt.savefig("WidthAgainstContactAngle.pdf", bbox_inches='tight', pad_inches=0.0)
