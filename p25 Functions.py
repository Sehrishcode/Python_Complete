# input('Hi there!')
print("Welcome new man!")
def greet_user():
    print("Hi there!!")
    print("Welcome abroad!")
print("Start")
greet_user()
print("Finish")
#parameters
def greet_user(first_name, last_name):
    print("Hi", first_name, last_name)
    print("Welcome abroad! Ms.",last_name)
print("Start")
greet_user("Erum","Ghani")
#key word arguement
def greet_user1(first_name, last_name):
    print("Hi", first_name, last_name)
    print("Welcome abroad! Ms.",last_name)
print("Start")
greet_user1(last_name="Erum",first_name="Ghani")
greet_user1("Erum",last_name= "Ghani")
#greet_user1(last_name="Erum","Ghani")
# return statement
def square(number):
    #return number*number
    print(number*number)
print(square(3))
