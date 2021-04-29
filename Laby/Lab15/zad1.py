class Restaurant():
    def __init__(self):
        pass

class IceCreamStand(Restaurant):
    flavours = ['Banana','Choco']
    def __init__(self):
        super().__init__()


    def show(self):
        i=1
        for x in self.flavours:
            print(f"{i}. {str(x)}")
            i+=1


class CoffeeShop(Restaurant):
    def __init__(self):
        super(Restaurant, self).__init__()


sp = IceCreamStand()
sp.show()