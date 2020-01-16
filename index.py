

class Product():

    def __init__(self, title):
        self.title = title
        self.description = ""


#every class has a default string property that is returned when you try to call print on the whole object, you can override that string property with __str__
    def __str__(self):
        return f"The {self.title} costs ${self.price}"

    @property # The getter
    def price(self):
        try:
            return self.__price # Note there are 2 underscores here
        except AttributeError:
            return 0

    @price.setter # The setter
    def price(self, new_price):
        if type(new_price) is float:
            self.__price = new_price
        else:
            raise TypeError('use a floating point type, you must')

car = Product("Mustang")


car.price = 5.5
car.price = 501.01
print(car) 

print(dir(car))