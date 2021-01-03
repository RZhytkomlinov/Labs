import random
print("zad1")
teams = ('Nuggets', 'Lakers', 'Warriors', 'Pistons', 'Mavericks', 'Kings', 'Clippers', 'Suns', 'Thunder',
         'Heat', 'Celtics', 'Bucks', 'Hornets', 'Bulls', 'Magic', 'Jazz', 'Rockets', 'Wizards', 'Hawks',
         'Nets','Cavaliers')
A = {0}
B = {0}
C = {0}
D = {0}
A.remove(0)
B.remove(0)
C.remove(0)
D.remove(0)
while len(D) < 10 or len(C) < 10 or len(B) < 10 or len(A) < 10:
    w1 = random.choice(teams)
    w2 = random.choice(teams)
    w3 = random.choice(teams)
    w4 = random.choice(teams)
    if w1 not in A and len(A) < 10:
        A.add(w1)
    if w2 not in B and len(B) < 10:
        B.add(w2)
    if w3 not in C and len(C) < 10:
        C.add(w3)
    if w4 not in D and len(D) < 10:
        D.add(w4)
print(A)
print(B)
print(C)
print(D)
AB = A.intersection(B)
CD = C.intersection(D)
intersection_set = AB.intersection(CD)
print(AB)
print(CD)
print(intersection_set)
#zad 2
print('zad2')
print('Difference: ', A.difference(B))
print('Union: ',C.union(D))
print('Issuperset: ',A.issuperset(C))
#zad 3
print('zad3')
print("Len A: ",len(A))
print("Len B: ",len(B))
print("Len C: ",len(C))
print("Len D: ",len(D))
if 'Clippers' in A:
    A.remove('Clippers')
print(A)
A_list = list(A)
print(A_list)

