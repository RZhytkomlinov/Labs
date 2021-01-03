# a = float(input("a:"))
# b = float(input("b:"))
# c = float(input("c:"))
# if (a == b):
#     print("a=b")
# elif (a == c):
#     print("a=c")
# elif (b == c):
#     print("b=c")
# elif a > b:
#     if a > c:
#         print("Największa a")
# elif b > a:
#     if b > c:
#         print("Największa b")
# elif c > a:
#     if c > b:
#         print("Największa c")
#         print("Największa c")
# else:
#     print("Największa c")


a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
if (a == b):
    print("a=b")
elif (a == c):
    print("a=c")
elif (b == c):
    print("b=c")
elif a < b:
    if b > c:
        print("Największa b")
    else:
        print("Największa c")
elif a > b:
    if a > c:
        print("Największa a")



