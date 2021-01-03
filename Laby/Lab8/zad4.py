import webbrowser
spam = {
    'person':'admin@gmail.com',
    'person1':'admin1@gmail.com',
    'person2':'admin2@gmail.com',
    'person3':'admin3@gmail.com',
    'person4':'admin4@gmail.com',
    'person5':'admin5@gmail.com',
}
with open('body.txt', 'r') as b:
    body = b.read()
    body = body.replace(' ', '%20')

def get_mail(person):

    mail = spam.get(person)
    return mail

subject = input('Podaj Subject:')

i = 0

for keys in spam:
    i +=1
    get_mail('person')
    print('Twój mail', i ,' to:')
    print('Adresat: ', get_mail(keys))
    print('Subject: ', subject)
    print('Text: ', body)
    webbrowser.open('mailto:?to=' + get_mail(keys) + '&subject=' + subject + '&body=' + body, new=1)


