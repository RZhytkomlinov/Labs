a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
d = float(input("d:"))

if a < b:
    if b > c:
        if ((c > d) or (d > c)):
            print("b największa")
    elif c > b:
        if c > d:
            print("c największa")
        elif ((d > c) and (d > b)):
            print("d największa")
else:
    print("a największa")

