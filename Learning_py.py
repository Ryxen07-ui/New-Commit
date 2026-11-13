# Class(blueprint) used to create --> Object
class Person:
    Name = None
    age = None
    def __init__(self, name, age): 
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"Name is {self.name}. Age is {self.age}"

# Object    
person1 = Person("Mg Mg", 20) # Object
person2 = Person("Aung Aung", 25)
# print(person)

# Access properties
print(person1)
print(person2)

# Modify Properties
person1.age = 25
person2.age = 18

# Delete Properties
del person1.age 
del person2.age

# Class pro Vs Object Pro
person1 = Person("Mg Mg")
person2 = Person("Aung Aung")

print(person1.species)
print(person2.species)

# Modify Class properties
person1 = Person("Mg Mg")
person2 = Person("Aung Aung")

Person.last.name = "Aung"

# Add New Properties 
person1.city = "Miami"
person2.city = "Florida"

