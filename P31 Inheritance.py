class Mamal:
    def walk(self):
        print("walk")
class Dog(Mamal):
    def bark(self):
        print("bark")
    
class Cat(Mamal):
    def be_annoying(self):
        print("annoying")
dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()
cat1.walk()