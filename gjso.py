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

""" class Hero: 
    def __init__(self, name, money, inventory): 
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item): 
        self.inventory.append(item)
        print(self.inventory)

Isaac = Hero("Isaac", 50000, ["quill"])
Isaac.buy({"title": "book", "pages": 90})
print(Isaac.__dict__ ) """

""" class Pet: 
    def __init__(self, name, happiness): 
        self.name = name
        self.__happiness = happiness
    def play(self, play): 
        self.__happiness += int(play)
    def show_status(self): 
        print(f"{self.name}) is {self.__happiness}")

Meow = Pet("Meow", 1)
Meow.play(play = 9)
print(Meow.__dict__ ) """

""" class Hero: 
    def __init__(self, name, money, inventory): 
        self.name = name
        self.__money = money
        self.__inventory = inventory
    def spend (self, item): 
        self.__inventory.append(item)
    def shh (self, spend):
        self.__money -= int(spend)
    def aa(self): 
        print(f"{self.name}) has {self.__money}")
Alfred = Hero("Alfred", 90, ["dagger"])
Alfred.shh(spend = 10)
Alfred.spend("bread")
print(Alfred.__dict__ ) """


""" class User: 
    def __init__(self, name, email): 
        self.name = name
        self.email = email

    def display_info(self): 
        return f"User: {self.name}, Email: {self.email}"


class Student(User): 
    def __init__(self, name, email, student_id): 
        super().__init__(name, email)
        self.student_id = student_id

    def display_info (self): 
        return f"Student: {self.name}, Email: {self.email}, Student ID: {self.student_id}"
    

class Teacher(User): 
    def __init__(self, name, email, subject): 
        super().__init__(name, email)
        self.subject = subject

    def display_info(self): 
        base_info = super().display_info()
        return f"{base_info}, Subject: {self.subject}"
        return f"Teacher: {self.name}, Email: {self.email}, Subject: {self.subject}"
    

class Administrator(User): 
    def __init__(self, name, email, role): 
        super().__init__(name,email)
        self.role = role

    def display_info(self): 
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self): 
        return f"{self.name} ({self.role}) is managing Kaub"
    

student = Student("Barry Williams", "barry@gnb.com", "HMSUNDAUNTED")
teacher = Teacher ("Jacob", "jacob@gnb.com", "Engineer")
administrator = Administrator("Karl", "unnamedprussianofficer@gnb.com", "Officer")

print(student.display_info())
print(teacher.display_info())
print(administrator.display_info())

admin = Administrator("Karl", "unnamedprussianofficer@gnb.com", "Officer")
print(admin.manage_system())

my_teacher = Teacher("Jacob", "jacob@gnb.com", "Engineer")
print(my_teacher.display_info()) """


class Pet: 
    def __init__(self, name, happiness = 10, hunger = 10, clean = 10, living = True):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self. clean = clean
        self.living = living
    def statDec(self): 
        self.clean -= 2
        self.happiness -= 4
        self.hunger -= 1
    def warnings(self): 
        if self.hunger <=5: 
            print(f"{self.name} is hungry...")
        if self.happiness <= 5: 
            print(f"{self.name} is unhappy...")
        if self.clean <= 5: 
            print(f"{self.name} is dirty...")
        if self.hunger >= 8: 
            print(f"{self.name} is full")
        if self.happiness >= 8: 
            print(f"{self.name} is happy")
        if self.clean >= 8: 
            print(f"{self.name} is so clean") 
print("*drops cat on you* here's your little pet, take care of it now.")
Userinput = input("Name your cat")
petOne = Pet(Userinput)
Userinput2 = True


while petOne.living == True: 
    petOne.warnings()
    Userinput = input(f"What would you like to do? clean, play, watch, or feed?")
    Userinput = Userinput.lower()
    if "clean" in Userinput: 
        print("*clean clean*") 
        petOne.clean=10
        petOne.happiness -=3
        petOne.statDec()
    elif "play" in Userinput: 
        print(f"yayayyay") 
        petOne.happiness += 5
        petOne.hunger -= 2
        petOne.clean -= 3
        if petOne.happiness > 10:
            petOne.happiness = 10
        petOne.statDec()
    elif "feed" in Userinput: 
        print("yumyum") 
        petOne.hunger = 10
        petOne.happiness +=3
        petOne.statDec()
    elif "watch" in Userinput: 
        petOne.statDec()
    else: 
        print("Sorry, invalid, try again") 
    if petOne.clean <= 0 or petOne.happiness <= 0 or petOne.hunger <= 0: 
        petOne.living = False
        break
    if petOne.clean <= 0: 
        petOne.living = False
        print(f"{petOne}'s hygiene was neglected") 
        break
    if petOne.hunger <= 0: 
        petOne.living = False
        print(f"{petOne} starved...") 
        break
    if petOne.happiness <= 0: 
        petOne.living = False
        print(f"{petOne} is too unhappy.") 
        break