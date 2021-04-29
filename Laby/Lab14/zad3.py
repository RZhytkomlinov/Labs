class Figure():
    def __init__(self):
        pass

    def perimeter(self):
        pass

    def area(self):
        pass

class Square(Figure):
    def __init__(self,a):
        super().__init__()
        self.a = a

    def perimeter(self):
        output = 4*self.a
        print(output)

    def area(self):
        output = pow(self.a,2)
        print(output)

class Circle(Figure):
    def __init__(self,r):
        super().__init__()
        self.r = r

    def perimeter(self):
        output = 2*3.14*self.r
        print(output)

    def area(self):
        output = 3.14*pow(self.r,2)
        print(output)

if __name__ == "__main__":
    first_choice = str(input("Wybierz figurę(kwadrat/kolo): "))
    second_choice = str(input("Co chcesz obliczyć(obwod/pole): "))
    if first_choice == 'kwadrat':
        side = int(input("Podaj długość jednej strony: "))
        kwadrat = Square(side)
        if second_choice == 'obwod':
            kwadrat.perimeter()
        elif second_choice == 'pole':
            kwadrat.area()
    elif first_choice == "kolo":
        r = int(input("Podaj r: "))
        kolo = Circle(r)
        if second_choice == 'obwod':
            kolo.perimeter()
        else:
            kolo.area()