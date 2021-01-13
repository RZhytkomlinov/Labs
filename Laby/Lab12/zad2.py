import math
def kula(r):
    v = 4/3*math.pi*math.pow(r,3)
    p = 4*math.pi*math.pow(r,2)
    finish = f'Objętość: {v}, Pole: {p}'
    return finish
def cube(a):
    v = math.pow(a,3)
    p = 6*math.pow(a,2)
    finish = f'Objętość: {v}, Pole: {p}'
    return finish
def stazek(r,h,l):
    v = 1/3*math.pi*math.pow(r,2)*h
    p = math.pi*r(r+l)
    finish = f'Objętość: {v}, Pole: {p}'
    return finish

what = input("Podaj co chcesz ode mnie: ")
if what == 'kula':
    r = int(input("Podaj r: "))
    print(kula(r))
elif what == 'sześcian' or what == 'szescian' or what == 'cube':
    a = int(input("Podaj a: "))
    print(cube(a))
elif what == 'stążek' or what == 'stazek':
    r = int(input("Podaj r: "))
    h = int(input("Podaj h: "))
    l = int(input("Podaj l: "))
    print(stazek(r,h,l))
else:
    print("Tu ci nie pomogę")


