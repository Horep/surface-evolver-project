import matplotlib.pyplot as plt
import numpy as np

def magphase(sinm,cosm):
    mag = np.sqrt(sinm**2 + cosm**2)
    phi = np.arctan2(sinm/mag, -cosm/mag)*180/np.pi
    return mag, phi


r_U = 0.5
rinv = 1/r_U

angle = np.array([0, 15, 30, 45, 60, 75, 89])
lower80 = rinv*np.array([0.507249114509187,0.507101953958448,0.506781822434329,0.506355040177250,0.505934767046276,0.505629605526488,0.505534549838011])
upper80 = rinv*np.array([0.387743704335652,0.386965887397995,0.386382234940210,0.385819833820649,0.384299272112938,0.383718304795563,0.383803277494628])

lower90 = rinv*np.array([0.548036922553003,0.547844525326969,0.547374777861100,0.546744724359917,0.546122283260744,0.545674031404370,0.545525142724897])
upper90 = rinv*np.array([0.417552997261284,0.416646595661471,0.415845633445687,0.415000140614035,0.413122310311690,0.412330199107599,0.412363689757834])

lower100 = rinv*np.array([0.591149508900952,0.590919761933186,0.590323682676273,0.589519774934674,0.588728479381457,0.588158817438974,0.587957161675631])
upper100 = rinv*np.array([0.441896521528020,0.440939872332147,0.439911679806059,0.438685215294136,0.436538808940269,0.435523168883089,0.435431129587071])

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
plt.savefig("WidthAgainstContactAngle.pdf", bbox_inches='tight', pad_inches=0.0)