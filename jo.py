class Footwear:
    def __init__(self, name, country, size):
        self.name = name
        self.country = country
        self.size = size

    def __repr__(self):
        print(''' This is the main fuse''')

    def paint(self):
        put = input('Please enter a color:\t')
        return print(f'Your {self.name} shoe is now {put!r} color')

    @property
    def reach(self):
        return self.size


class Shirt(Footwear):
    def __init__(self):
        pass


shoe1 = Footwear('Balenciaga', 'France', 1997)
shoe2 = Footwear('Dior', 'Belgium', 1987)

print(shoe1.country, shoe2.name)
print(shoe1.size, shoe2.country)
print(shoe2.reach)

shoe1.paint(), shoe2.paint()
