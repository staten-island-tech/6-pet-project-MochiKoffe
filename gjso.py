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
    def __init__(self, name, happiness): 
        self.name = name
        self.__happiness = happiness
    def play(self, play): 
        self.__happiness += int(play)
    def show_status(self): 
        print(f"{self.name}) is {self.__happiness}")

Bauwow = Pet("Bauwow", 1)
Bauwow.play(play = 9)
print(Bauwow.__dict__ )