import math
import numpy as np
import matplotlib.pyplot as plt
import random
PI = math.pi
min_theta = -PI/2
max_theta = +PI/2
steps = 10000
step_theta = (max_theta-min_theta)/steps
wl = 4*10**-7 #input("Enter wavelength of the light: ")
a = 10**-6 #input("Enter width of slits: ")
d = 10**-5 #input("Enter distance between slits: ")
D = 0.8 #input("Enter distance between slits and the screen: ")
I_initial = 1 #input("Enter initial intensity of light: ")
Theta = min_theta #math.atan(x/D)
N_photon = 10000
N_hits = 0
One_or_Two = 0
Y = True
N = False
One_or_Two = input("Is a slit covered (Y/N): ")

if One_or_Two == Y:
	One_or_Two = True
	
else:
	One_or_Two = False

X_rand = 0
Y_rand = 0

X = []
Y = []

def two_slits(Angle):
	p = (PI*d*math.sin(Angle))/(wl)
	q = PI*a*math.sin(Angle)/wl
	s = pow(math.cos(p),2)
	t = pow((math.sin(q)/q),2)
	return I_initial*s*t
	
def one_slit(angle):
	p = (PI*d*math.sin(angle))/(wl)
	s = pow(math.cos(p),2)
	return I_initial*s

def experiment(N):
	Box = [[0 for m in range(0, 2) ] for n in range(0,N)]
	while N_hits != N:
		X_rand = random.uniform(min_theta,max_theta)
		Y_rand = random.uniform(0,1)
		if two_slits(X_rand)>= Y_rand:
			Box[N_hits] = [X_rand, Y_rand]
			N_hits = N_hits + 1
	return Box

if One_or_Two == True:
	for x in range (0, steps):	
		X.append(Theta)
		Y.append(one_slit(Theta))
		Theta= Theta + step_theta
	plt.plot(X,Y)
	plt.show()
else:
	for x in range (0, steps):	
		X.append(Theta)
		Y.append(two_slits(Theta))
		Theta= Theta + step_theta

	plt.plot(X,Y)
	plt.show()
	plt.scatter(experiment(N_photon))
	plt.show()
