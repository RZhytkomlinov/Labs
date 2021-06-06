import linecache

try:
    f1 = open('invo.txt', 'r', encoding='utf-8')
    f2 = open('art2.txt', 'r', encoding='utf-8')
    with open("zad2_result.txt", 'w') as f3:
        for i,(f1,f2) in enumerate(zip(f1,f2)):
            f3.writelines(linecache.getline('art1.txt', i))
            f3.writelines(linecache.getline('art2.txt', i))
            print(linecache.getline('art1.txt', i))
            print(linecache.getline('art2.txt', i))
except:
    print("Podałeś złe nazwy plików")
