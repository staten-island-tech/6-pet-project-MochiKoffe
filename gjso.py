""" class Calculator():
    def add(x,y): 
        print(x+y)
        return x+y
    def add_many(numbers): 
        print(sum(numbers))
        return sum(numbers)
    def subtract (numbers):
        return numbers
Calculator.add(5,6) """

""" class Hero:
    def __init__(self, name, money, inventory): 
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item): 
        self.inventory.append(item)
        print(self.inventory)

Jillian = Hero("Jillian", 150, ["potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__ ) """

""" class BankAccount: 
    def __init__(self, owner, balance): 
        self.owner = owner
        self.__balance = balance 
    def deposit(self, amount): 
        self.__balance += amount
    def show_balance(self): 
        print(f"{self.owner}) has ${self.__balance}")

sabrina = BankAccount("Sabrina", 2)
sabrina.deposit({"amount": 67})
print(sabrina.__dict__ ) """

class Hero: 
    def __init__(self, name, money, inventory): 
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item): 
        self.inventory.append(item)
        print(self.inventory)

Isaac = Hero("Isaac", 50000, ["quill"])
Isaac.buy({"title": "book", "pages": 90})
print(Isaac.__dict__ )

class Pet: 
    def __init__(self, name, happiness): 
        self.name = name
        self.__happiness = happiness
    def play(self, play): 
        self.__happiness += int(play)
    def show_status(self): 
        print(f"{self.name}) is {self.__happiness}")

Meow = Pet("Meow", 1)
Meow.play(play = 9)
print(Meow.__dict__ )

class Hero: 
    def __init__(self, name, money, inventory): 
        self.name = name
        self.__money = money
        self.__inventory = inventory
    def spend (self, price, item): 
        self.__inventory.append(item)
        self.__money -= int(price)
    def aa(self): 
        print(f"{self.name}) has {self.__money}")
Alfred = Hero("Alfred", 90, ["dagger"])
Alfred.spend(price = 10)
Alfred.spend(item = ({"bread": "food", "hunger": 20}))
print(Alfred.__dict__ )