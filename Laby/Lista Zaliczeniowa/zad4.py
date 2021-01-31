def gb():
    while True:
        try:
            gb_input = int(input("Podaj pojemność w GB: "))
            b_fake = gb_input * pow(10, 9)
            if gb_input >= 1:
                gb_real = b_fake / pow(1024, 3)
                print(f"Realna pojemność takiego dysku {round(gb_real, 2)} GB")
                break
            else:
                print("Wpisałeś 0 albo ujemną liczbę, podaj jeszcze raz")
        except:
            print("Musisz wpisać tylko cyferki")


def tb():
    while True:
        try:
            tb_input = int(input("Podaj pojemność w TB: "))
            b_fake = tb_input * pow(10, 12)
            if tb_input == 1:
                tb_real = b_fake / pow(1024, 3)
                print(f"Realna pojemność takiego dysku {round(tb_real, 2)} TB")
                break
            elif tb_input > 1:
                tb_real = b_fake / pow(1024, 4)
                print(f"Realna pojemność takiego dysku {round(tb_real, 2)} TB")
                break
            else:
                print("Wpisałeś 0 albo ujemną liczbę, podaj jeszcze raz")
        except:
            print("Musisz wpisać tylko cyferki")


print("Obliczamy realną pojemność dysków:")
print("Liczymy TB(wpisz 'tb') czy GB(wpisz 'gb')?")
while True:
    calc = str(input('tb/gb :'))
    try:
        if calc == 'tb':
            tb()
            break
        elif calc == 'gb':
            gb()
            break
        else:
            print("Wpisz 'tb' albo 'gb': ")
    except TypeError:
        print("Wpisz 'tb' albo 'gb': ")
