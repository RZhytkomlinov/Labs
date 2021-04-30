shs = []

class Sh():

    def __init__(self, name, powers):
        self.name = name
        self.powers = powers

    def add_to(self):
        shs.append(self.name)
        print(f'{self.name} został dodany do tablicy')

    def give_sp(self):
        self.powers = True
        print(f'{self.name} dostaje supersiłe')

    def take_sp(self):
        self.powers = False
        print(f'{self.name} stracił supersiłe')


class Spiderman(Sh):
    def __init__(self, name, powers):
        super().__init__(name, powers)

    def strzela(self):
        print(f'{self.name} strzela pajączyną')


if __name__ == "__main__":
    spiderman = Spiderman('Spiderman', True)
    spiderman.add_to()
    spiderman.take_sp()
    spiderman.give_sp()
    spiderman.strzela()
    print(shs)
