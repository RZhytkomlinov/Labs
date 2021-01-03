import random

randomList = random.sample(range(0,50), 10)
print("Lista przed zmieszaniem: ", randomList)
random.shuffle(randomList)
print("Pomieszana lista: ", randomList)
randomList.sort()
print("Posortowana lista:", randomList) 