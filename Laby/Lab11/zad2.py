from pytemp import pytemp
inp_cel = int(input("Celcius: "))
f = pytemp(inp_cel, 'c', 'f')
if f >= 212:
    print("Woda wrze")
elif f < 32:
    print("Woda zamarza")
else:
    print("cool")

#Kelvin -> Fahrenheit
f = pytemp(40,'k', 'f')
#Fahrenheit -> Kelvin
k = pytemp(f,'f','k')
#Celcius -> Kelvin
c = pytemp(40,'k', 'c')
#Kelvin -> Celcius
k1 = pytemp(c,'c','k')
