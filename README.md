# surface-evolver-project
This is a place for me to store some work using Surface Evolver.

This code, "twocylinders" is designed to calculate the minimal droplet surface between two fibers.
The angle between the two fibers can be changed by rotating the upper cylinder in the x-y plane.
The contact angle between the fiber and the droplet can be adjusted.
The density of the fluid can be changed.
The initial size of the droplet can also be changed if it is too far from the minimal surface using "rad_center"

An assumption made in the integral derivation is that the liquid-surface areas are on the lower part of the upper cylinder, and upper part of the lower cylinder.

The gravity can be disabled by setting GZ = -0.

To run the code, simply load the file with surface evolver and type "calc" after configuring parameters if needed.

To shrink the droplet until it detaches, use code "auto_shrink". 

To detach manually, use "separatelower" or "separateupper" to detach from the respective cylinder.

In the "Python Scripts" folder there are scripts related to plotting data retrieved from the Surface Evolver model. The data is located within the scripts already, and the code needs only be executed.
