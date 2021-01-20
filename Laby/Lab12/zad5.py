def run():
    while True:
        try:
            masa = float(input("Wprowadź swoją wagę w kilogramach: "))
        except ValueError:
            continue
        else:
            if masa < 0:
                print("Niewłaściwa wartość")
                continue
            else:
                break

    while True:
        try:
            wzrost = float(input("Wprowadź swój wzrost w metrach: "))
        except ValueError:
            continue
        else:
            if wzrost < 0:
                print("Niewłaściwa wartość")
                continue
            else:
                break

    bmi = masa / (wzrost * wzrost)

    if bmi < 18.5:
        print("Masz niedowagę.")
    elif 18.5 <= bmi < 25:
        print("Twoja waga jest prawidłowa")
    elif 25 <= bmi < 30:
        print("Masz nadwagę!!!")


run()