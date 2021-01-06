import random
list = []
while True:
    x = (random.randint(0,1))
    list.append(x)
    if len(list) == 50:
        print(list)
        break