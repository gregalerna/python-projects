##################################################
#Jorge Vera Moreno                               #
#10/12/15                                        #
#Numerical simulation of planetary orbits        #
##################################################

from visual import sphere, vector, color, rate, mag

dt = 0.0001 # timestep
step = 1 # loop counter
maxstep = 8000 # maximum number of steps
#  Define the star, planets and constants
M = 1000 # mass of star (in units where G = 1)
mass1 = 1 # mass of first planet
mass2 = 50 # mass of second planet
initpos = vector(0,1,0) # initial position vector of Planet
Sinitpos = vector(0,2,0) # initial position vector of Second Planet
Planet = sphere(pos=initpos,radius=0.02,color=color.blue,make_trail=True)#Graphic visualisation of Planet 1
Planet.trail_object.color=color.white # make Planet 1's trail white
SecondPlanet = sphere(pos=Sinitpos,radius=0.05,color=color.cyan,make_trail=True)#Graphic visualisation of Planet 2
SecondPlanet.trail_object.color=color.red # make Planet 2's trail red
Star = sphere(pos=(0,0,0),radius=0.08,color=color.yellow)#Graphic visualisation of Star
vel = vector(-15, 0, 0) # initial velocity of planet 1
Svel = vector(-60, 0, 0) # initial velocity of planet 1
r=initpos #Position vector for Planet 1
r2=Sinitpos #Position vector for Planet 2
while step <= maxstep: #Run simulation in time limit defined by maximum step
    Planet.pos=r #Set the 3D objects' location according to position vectors
    SecondPlanet.pos=r2
    vel=vel-(M*mass1/(mag(r)**3))*r*dt+(mass1*mass2/(mag(r2-r)**3))*(r2-r)*dt #Velocity variation according to Newton's laws
    #Radially inwards interaction from star, outwards from second planet
    Svel=Svel-(M*mass2/(mag(r2)**3))*r2*dt+(mass1*mass2/(mag(r2-r)**3))*(r2-r)*dt
    #Radially inwards interaction from star and first planet
    r+=dt*vel #Update position vectors
    r2+=dt*Svel
    step+=1 #Update step
    rate(75) #Fast animation
print("end of program")