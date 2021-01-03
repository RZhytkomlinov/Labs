contacts = {
    'Pan Dough': 1,
    'SAN FRANCISCO STYLE DOUGH': 2,
    'DOUGH WITH CHEESE IN CRUST': 31,
    'MARGHERITA': 14,
    'AMERICANA': 15,
    'PEPPERONI': 16,
    'CLASSICA': 17,
    'HAWAIIAN': 18,
    'HOT PEPPERONI': 19,
    'SUPREME': 32
}
for keys in contacts.keys():
    print(keys)

for values in contacts.values():
    print(values)

for items in contacts.items():
    print(items)

key = input("Podaj nazwe: ")
value = float(input("Podaj cene: "))
contacts[key] = value

max_v = max(contacts.values())
min_v = min(contacts.values())
max_k = max(keys for keys, values in contacts.items() if values == max_v)
min_k = min(keys for keys, values in contacts.items() if values == min_v)
# del contacts[max(contacts, key = contacts.get)]
# del contacts[min(contacts, key = contacts.get)]
del contacts[max_k]
del contacts[min_k]

print(contacts)

