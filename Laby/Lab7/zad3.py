import random

list_np = []
list_p = []
while len(list_np) < 101:
    int_rand = int(random.randint(0, 100))
    if int_rand % 2 != 0:
        list_np.append(int_rand)
while len(list_p) < 101:
    int_rand = int(random.randint(0, 100))
    if (int_rand % 2) == 0:
        list_p.append(int_rand)


tuplaA = tuple(list_p)
tuplaB = tuple(list_np)
print("Liczby parzyste: ")
print(tuplaA)
print("Liczby nieparzyste: ")
print(tuplaB)

tuplaC = tuplaA + tuplaB
print(tuplaC)
count_0 = tuplaC.count(0)
count_100 = tuplaC.count(100)
print("Liczba 0 wystąpiła: ",count_0)
print("Liczba 100 wystąpiła: ",count_100)
i = 0
index_list_0 =[]
index_list_100 =[]
index_list_C0 = []
index_list_C100 = []
for i in range (0, len(tuplaA)):
    if tuplaA[i] == 0:
        index_list_0.append(id(tuplaA[i]))
    elif tuplaA[i] == 100:
        index_list_100.append(id(tuplaA[i]))
    i += 1
for i in range (0, len(tuplaC)):
    if tuplaC[i] == 0:
        index_list_C0.append(id(tuplaC[i]))
    elif tuplaC[i] == 100:
        index_list_C100.append(id(tuplaC[i]))
    i += 1
print(index_list_0)
print(index_list_100)
print(index_list_C0)
print(index_list_C100)