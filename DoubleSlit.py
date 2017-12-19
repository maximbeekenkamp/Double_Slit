import math
import numpy as np
import matplotlib.pyplot as plt
a = 1
b = 100
#c = 299792458
#h = 6.62607004*10**-34
wl = 6.4*10**-7 #input("Enter wavelength of the light: ")
#E = h*f
#x = 0.03
W = 7*10**-7 #input("Enter width of slits: ")
d = 2.8*10**-6 #input("Enter distance between slits: ")
D = 0.8 #input("Enter distance between slits and the screen: ")
I_initial = input("Enter initial intensity of light: ") 
Theta = 0.01 #math.atan(x/D) 
#F = [[0 for m in range(0,a+1) ] for n in range(0,b)]
I = []#[[0 for m in range(0,a) ] for n in range(0,b)]

X = []
Y = []


for x in range (0, b):
	p = (math.pi*d*math.sin(Theta))/(wl)
	q = math.pi*W*math.sin(Theta/wl)
	r = math.pi*W*math.sin(Theta/wl)
	s = math.cos(p)**2
	t = ((math.sin(q))/(r))**2	
	I.append(I_initial*s*t)
	print (I[x])
	Y.append(I[x])
	X.append(Theta)
	Theta = Theta + 0.01

plt.plot(X,Y)
plt.show()
