import linecache

x = open("invo.txt", 'r', encoding='utf-8')

for i,x in enumerate(x):
    if i == 7:
        print(linecache.getline('invo.txt', 8))
    elif i == 11:
        print(linecache.getline('invo.txt', 12))
    elif i == 59:
        print(linecache.getline('invo.txt', 60))
    elif i == 93:
        print(linecache.getline('invo.txt', 98))
    elif i == 103:
        print(linecache.getline('invo.txt', 104))

