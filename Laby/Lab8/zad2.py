contacts = {
    'a': 1,
    'b': 2,
    'c': 31,
    'd': 14,
    'e': 15,
    'f': 16,
    'g': 17,
    'h': 18,
    'k': 19,
}
x = len(contacts)
print(contacts)
contacts['a'] = 2
print(contacts)
if x % 2 != 0:
    del contacts[x/2]
print(contacts)