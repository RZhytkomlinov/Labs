import webbrowser
users = {
    'admin':'admin',
    'bbb':'bbb',
    'ccc':'ccc',
    'ddd':'ddd',
    'eee':'eee',
    'fff':'fff',
}
login = input('podaj login: ')
passw = input('podaj password: ')
if login in users.keys() and passw in users.values():
    print('nice')
    if login == 'admin' and passw == 'admin':
        webbrowser.open('admin.html')
    else:
        webbrowser.open('nie_admin.html')
else:
    print('not nice')
    webbrowser.open('invalid.html')