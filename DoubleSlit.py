import math

c = 299792458
#h = 6.62607004*10**-34
wl = 6.4*10**-7 #input("Enter wavelength of the light: ")
#E = h*f
#x = 0.03
W = 7*10**-7 #input("Enter width of slits: ")
d = 2.8*10**-6 #input("Enter distance between slits: ")
D = 0.8 #input("Enter distance between slits and the screen: ")
I_initial = input("Enter initial intensity of light: ") 
Theta = 1 #math.atan(x/D) 
for k in range (0, 100):
	I = I_initial*math.cos(((math.pi*d*math.sin(Theta))/(wl))*(((math.sin(math.pi*W*math.sin(Theta/wl))/(math.pi*W*math.sin(Theta/wl))))**2))**2
	print (I)
	Theta = Theta + 0.01

