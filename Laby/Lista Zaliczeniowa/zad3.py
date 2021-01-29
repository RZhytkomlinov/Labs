def quiz():
    correct = 0
    answers = ['a','c','a','b','c','a','b','a','c','b']
    questions = ["Czy patrzysz teraz w monitor?",
                "1 GB to ile MB:",
                "Czy dałeś radę zainstalować Pythona sam?",
                "Czy dałeś radę podpiąć GitHub sam?",
                "PyCharm>VSCode?",
                "Czy wiesz jakie jeszcze pytania tu dać?",
                "Czy korszystasz teraz z myszki?",
                "Czy korszystasz teraz z klawiatury?",
                "Co chcesz dostać z tego testu?",
                "Ostatnie pytanie:Czy podobał ci się quiz?"]
    choices =  ["a) - 'Tak' b) - 'Nie' c) - 'Nie wiem'",
                "a) - '1000' b) - '2000' c) - '1024'",
                "a) - 'Tak' b) - 'Nie' c) - 'Nie, ale c'",
                "a) - 'Nie'  b) - 'Tak i prawie kosztowało mi to życia' c) - 'Help'",
                "a) - 'Korzystam z IDLE' b) - 'Nie' c) - 'Tak'",
                "a) - 'Nie' b) - 'Tak' c) - *dies from depression*",
                "a) - 'Tak' b) - 'Nie' c) - *angry touchpad noises*",
                "a) - 'Tak' b) - 'Nie' c) - *angry Onscreen Keyboard noises*",
                "a) - '5' b) - '6' c) - 'Daj mi skończyć, proszę'",
                "a) - 'Tak' b) - 'Nie' c) - 'Jak najbardziej'"]

    for i in range (0,len(answers)):
        print(questions[i])
        print(choices[i])
        answer = input("Podaj odpowiedź: ")
        if answer == answers[i]:
            correct +=1
    print("Correct answers: ",correct)
    if correct == 10:
        print("Twoja ocena - 6")
    elif 7<=correct<=9:
        print("Twoja ocena - 5")
    elif correct == 6:
        print("Twoja ocena - 4")
    elif correct == 4 or correct == 5:
        print("Twoja ocena - 3")
    elif correct == 3:
        print("Twoja ocena - 2")
    else:
        print("Twoja ocena - 1")



print("Quiz informatyczny")
print("Jak nie zdasz, to nie zdajesz semestru")
quiz()
