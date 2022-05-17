import matplotlib.pyplot as plt
import numpy as np
def magphase(sinm,cosm):
    mag = np.sqrt(sinm**2 + cosm**2)
    phi = np.arctan2(sinm/mag, -cosm/mag)*180/np.pi
    return mag, phi


r_U = 0.5
rinv = 1/r_U

angle = np.array([0, 15, 30, 45, 60, 75, 89])
lower80 = rinv*np.array([0.476305791966493,0.476035035983167,0.475305881908765,0.474319004032185,0.473339826753453,0.472627164096327,0.472368795548632])
upper80 = rinv*np.array([0.476305785040563,0.475558969482824,0.474879627996795,0.474319019995003,0.472868529342320,0.472201843677773,0.472305002463392])

lower90 = rinv*np.array([0.510468375757193,0.510135865211322,0.509230372938627,0.508003821905316,0.506788987771113,0.505904874463303,0.505582010652648])
upper90 = rinv*np.array([0.510468376940597,0.509751649080283,0.508889299258328,0.508004145658504,0.506401770360752,0.505557940975235,0.505512737825747])

lower100 = rinv*np.array([0.544481909430045,0.544091115745318,0.543023223164506,0.541574385374148,0.540138228561339,0.539095181848706,0.538717179569994])
upper100 = rinv*np.array([0.544481899149833,0.543872795146972,0.542851716030689,0.541574328418605,0.539910737190860,0.538909237709610,0.538642009560863])

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


plt.plot(angle, lower80, marker="v", linestyle='None', label=r"$\theta_{YL} = 80\degree$ L", color='blue')
plt.plot(angle, lower90, marker="v", linestyle='None', label=r"$\theta_{YL} = 90\degree$ L", color='orange')
plt.plot(angle, lower100, marker="v", linestyle='None', label=r"$\theta_{YL} = 100\degree$ L", color='green')

plt.plot(angle, upper80, marker="^", linestyle='None', label=r"$\theta_{YL} = 80\degree$ U", color='blue')
plt.plot(angle, upper90, marker="^", linestyle='None', label=r"$\theta_{YL} = 90\degree$ U", color='orange')
plt.plot(angle, upper100, marker="^", linestyle='None', label=r"$\theta_{YL} = 100\degree$ U", color='green')




plt.ylabel(r"Width/$r_{U}$")
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.legend(bbox_to_anchor=(1,1))
plt.savefig("WidthAgainstContactAngleNoGrav.pdf", bbox_inches='tight', pad_inches=0.0)
