import random
for i in range (3):
    print(random.random())
    print(random.randint(10,20))
members = [ "Bob", "John", "Mary", "Mosh"]
leader = random.choice(members)
print(leader)