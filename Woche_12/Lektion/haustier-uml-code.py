class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_Pet(self, pet: "Pet"):
        pet.owner = self # setzt owner
        self.pets.append(pet)
    
    def list_Pets(self):
        # return self.pets
        return [p.name for p in self.pets]

class Pet:
    def __init__(self, name=str, age=int, owner: "Owner" = None):
        self.name = name
        self.age = age
        self.owner = owner

    def speak(self):
        return "..." # wird von Unterklasse überschrieben
    
    def info(self):
        return f"{self.name} ({self.age} Jahre)"

class Cat(Pet):
    def __init__(self, name=str, age=int, color=str, owner: "Owner" = None):
        super().__init__(name, age, owner)
        self.color = color

    def speak(self):
        return "Miau!"

class Dog(Pet):
    def __init__(self, name=str, age=int, breed=str, owner: "Owner" = None):
        super().__init__(name, age, owner)
        self.breed = breed

    def speak(self):
        return "Wuff!"

anna = Owner("Anna")

rex = Dog("Rex", 6, "Golden Retriever")
bagger = Cat("Baggerli", 13, "Schildpatt")

anna.add_Pet(bagger)
anna.add_Pet(rex)

print(anna.list_Pets())
print(rex.speak())
print(bagger.info())