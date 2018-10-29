############################################################
#Jorge Vera Moreno                                         #
#3/12/2015                                                 #
#3D visualisation of a projectile using VPython            #
############################################################

from visual import sphere, curve, color, display, rate
import numpy as np

# set up the scene
scene = display(x = 50, y = 50, width = 640, height = 480, center = (20,0,0))
ground = curve(pos=[(-5,0,0),(50,0,0)],color = color.green)

# initial ball coordinates (metres)
x0 = float(raw_input("Input the initial horizontal position in m: ")) #Set value for horizontal position
y0 = 0.0 #Initial height is 0
y = y0 #Declare y
g = 9.8 # gravitational acceleration, m/s2
dt = float(raw_input("Input the time interval in s: ")) #Time interval for loop, in seconds
e=float(raw_input("Input the coeffcient of restitution: ")) #Set value for coefficient of restitution
dtheta = float(raw_input("Input the initial angle in degrees: ")) #Set value for theta in degrees
theta = np.radians(dtheta) #Turn dtheta into radians
v0 = float(raw_input("Input the initial velocity in metres/second: ")) #Set initial velocity
vInitial=v0 #Store initial velocity in another variable (useful for final calculations)
# start the animation
ball = sphere(pos = (x0,y0,0),radius = 1,make_trail=True)
t = 0 # initial time
tList=[] #List that stores all the times the ball bounces
while v0 >= 0.01: #Play animation while velocity is higher than 0.01
#Irrelevant to repeat animation at that point
    while y>=y0: #While actual height is greater or equal to initial height
        x=x0+v0*t*np.cos(theta) #Equations of motion for a projectile
        y=y0+v0*t*np.sin(theta)-0.5*g*(t**2)
        ball.pos=(x,y,0)
        t+=dt #Update time
        rate(45) #Fast animation
        #When the loop is broken, the ball reaches the ground
    tList.append(t) #Add time the ball bounces
    incidenceAngle=(np.pi/2)-theta #Landing angle
    reflectionAngle=np.arctan(np.tan(incidenceAngle)/e) #Reflected angle
    vPrime=(np.cos(incidenceAngle)/np.cos(reflectionAngle))*v0*e #New velocity for bounce
    thetaPrime=(np.pi/2)-reflectionAngle #New angle for bounce
    v0=vPrime #New velocity for calculations in loop
    theta=thetaPrime #New angle for calculations in loop
    y=0 #Set actual height to ground
    x0=x #Set actual horizontal position
    t=0 #Update time
theta = np.radians(dtheta) #Restore theta to old value for calculation

Range=(np.sin(2*np.radians(dtheta))*(vInitial)**2)/g #Find out range for first bounce

print "The range for the first bounce is",Range,"m .The last horizontal position was",x,"m .The ball was in the air for",np.sum(tList),"s"