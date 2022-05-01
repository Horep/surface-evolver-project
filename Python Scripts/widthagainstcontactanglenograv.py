import matplotlib.pyplot as plt
import numpy as np

def magphase(sinm,cosm):
    mag = np.sqrt(sinm**2 + cosm**2)
    phi = np.arctan2(sinm/mag, -cosm/mag)*180/np.pi
    return mag, phi


r_U = 0.5
rinv = 1/r_U

angle = np.array([0, 15, 30, 45, 60, 75, 89])
lower80 = rinv*np.array([0.470035265524425,0.469789200107754,0.469117317645810,0.468206975143370,0.467304917690820,0.466648879833296,0.466410257833280])
upper80 = rinv*np.array([0.481167111058717,0.480297121617503,0.479706291900660,0.479250710030912,0.477687806976048,0.477113959890341,0.477294655834820])

lower90 = rinv*np.array([0.510490197694461,0.510156039298431,0.509248277992837,0.508019058554976,0.506801050995727,0.505913204264496,0.505594797437912])
upper90 = rinv*np.array([0.510490201322993,0.509644872088391,0.508862067863610,0.508019327682798,0.506271274314366,0.505505552306247,0.505508822274560])

lower100 = rinv*np.array([0.552688469440878,0.552271677038883,0.551142267858579,0.549618182825564,0.548114980433339,0.547028013837523,0.546635304821853])
upper100 = rinv*np.array([0.538142366540952,0.537410057851668,0.536426660580389,0.535096712322497,0.533250717784211,0.532297637499022,0.532029974536172])

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


#plt.plot(angle,lower80)
#plt.plot(angle,lower90)
#plt.plot(angle,lower100)

plt.plot(angle, lower80, marker="^", linestyle='None', label=r"$\theta_{YL} = 80\degree$ L", color='orange')
plt.plot(angle, lower90, marker="^", linestyle='None', label=r"$\theta_{YL} = 90\degree$ L", color='blue')
plt.plot(angle, lower100, marker="^", linestyle='None', label=r"$\theta_{YL} = 100\degree$ L", color='green')

plt.plot(angle, upper80, marker="v", linestyle='None', label=r"$\theta_{YL} = 80\degree$ U", color='orange')
plt.plot(angle, upper90, marker="v", linestyle='None', label=r"$\theta_{YL} = 90\degree$ U", color='blue')
plt.plot(angle, upper100, marker="v", linestyle='None', label=r"$\theta_{YL} = 100\degree$ U", color='green')

plt.ylabel(r"Width/$r_{U}$")
plt.xlabel(r"Cylinder Angle $(\vartheta\degree)$")
plt.legend(bbox_to_anchor=(1,1))
plt.savefig("WidthAgainstContactAngleNoGrav.pdf", bbox_inches='tight', pad_inches=0.0)