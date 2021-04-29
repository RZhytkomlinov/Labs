
class Animal():
    def __init__(self, specie, name, age, weight, able_to_fly):
        self.specie = specie
        self.name = name
        self.age = age
        self.weight = weight
        self.able_to_fly = able_to_fly

    def voice(self):
        pass
    def introduce(self):
        print(f'Hi, I am a {self.specie} named {self.name}')
        self.voice()
    def is_fly(self):
        if self.able_to_fly == True:
            print(f'{self.specie} named {self.name} lata')
        else:
            print(f'{self.specie} named {self.name} nie lata')

class Cat(Animal):
    def __init__(self, specie, name, age, weight, able_to_fly):
        super().__init__(specie, name, age, weight, able_to_fly)

    def voice(self):
        print('Meow')


class Fish(Animal):
    def __init__(self, specie, name, age, weight,able_to_fly):
        super().__init__(specie, name, age, weight,able_to_fly)

    def voice(self):
        print('Blrb blrb')


class Dog(Animal):
    def __init__(self, specie, name, age, weight,able_to_fly):
        super().__init__(specie, name, age, weight,able_to_fly)

    def voice(self):
        print('Woof')


class Bird(Animal):
    def __init__(self, specie, name, age, weight,able_to_fly):
        super().__init__(specie, name, age, weight,able_to_fly)

    def voice(self):
        print('*bird noises*')

if __name__ == "__main__":
    dog = Dog('Dog', 'Temmie', '20','20', False)
    cat = Cat('Cat', 'Mimi', '20', '20', False)
    bird = Bird('Bird', 'Oscar', '20', '20', True)
    fish = Fish('Fish', 'Forkie', '20', '20', False)
    dog.introduce()
    bird.introduce()
    dog.is_fly()
    bird.is_fly()
