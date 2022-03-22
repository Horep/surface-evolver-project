# surface-evolver-project
This is a place for me to store some work using Surface Evolver.

This code, "twocylinders" is designed to calculate a minimal droplet surface between two fibers.
The angle between the two fibers can be changed by rotating the upper cylinder in the x-y plane.
The contact angle between the fiber and the droplet can be adjusted.
The density of the fluid can be changed.
The initial size of the droplet can also be changed if it is too far from the minimal surface using "rad_center"

An assumption made in the integral derivation is that the liquid-surface areas are on the lower part of the upper cylinder, and upper part of the lower cylinder.

At the time of writing the gravity (G=0) needs to be set to zero, as the potential integrals have not been implemented. This is done in the "calc" command.

To run the code, simply load the file with surface evolver and type "calc" after configuring parameters if needed.

TODO: Implement gravitational potential energy integrals, check signs on all contact angle integrals.
