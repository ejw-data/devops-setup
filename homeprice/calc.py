PRICE_PER_SQFT = 1250


class House:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def min_price(self):
        self.price = self.size * PRICE_PER_SQFT

    def buy(self):
        return self.size * PRICE_PER_SQFT < 500000
