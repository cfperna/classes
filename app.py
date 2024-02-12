class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('price cannot be negative')
        self.__price = value


product = Product(10)
print(product.price)
product2 = Product(20)
print(product2.price)

