tab3 = []
i = 0
while i<11:
    a = int(input("daj x: "))
    if a>60 or a<-1:
        print("Debilu, nie taki x, jesteś zjebany")
        continue
    else:
        tab3.append(a)
        i +=1
print(tab3)
insert = 0
while insert < 4:
    where = int(input("daj where"))
    what = input("daj what")
    insert += 1
    tab3.insert(where, what)
print(tab3)
append = 0
while append < 4:
    where = int(input("daj where"))
    what = input("daj what")
    append += 1
    tab3.append(where, what)
print(tab3)
remove = 0
while remove < 4:
    where = int(input("daj where"))
    what = input("daj what")
    remove += 1
    tab3.remove(where, what)
print(tab3)
pop = 0
while pop < 4:
    where = int(input("daj where"))
    what = input("daj what")
    pop += 1
    tab3.pop(where, what)
print(tab3)


