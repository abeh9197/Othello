class Thing:
    pass

example = Thing
print(Thing)
print(example)

class Thing2:
    letters = 'abc'

print(Thing2.letters)

class Thing3:
    def __init__(self, letters):
        self.letters = letters

example3 = Thing3(letters = 'xyz')
print(example3.letters)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self, name, symbol,number):
        print(self.name, self.symbol, self.number)



d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(d)
hydrogen.dump()

