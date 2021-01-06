numb = []
for i in range (1001):
    if i %2 !=0 and i % 3 !=0 and i % 5 !=0 and i % 7 !=0:
        if i<1000:
            numb.append(i)

print(max(numb))