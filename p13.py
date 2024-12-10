class Fruit:
    def __new__(cls):
        obj = super().__new__(Flower) # Flower is another class
        return obj # return the object
frt1 = Fruit()