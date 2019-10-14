class Store(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def percent(self):
        new_price = self.price + self.price*0.2
        return self.name, new_price

    def consignment(self, quantity):
        index = quantity // 10
        quantity = quantity - index
        cons = quantity * self.price
        return self.name, cons


if __name__ == "__main__":
    s = Store("milk", 5)
    q = int(input('q = '))
    print(s.percent())
    print(s.consignment(q))



