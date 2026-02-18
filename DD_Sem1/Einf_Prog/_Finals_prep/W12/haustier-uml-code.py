class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: "Pet"):
        pet.owner = self   # Owner wird gesetzt
        self.pets.append(pet)

    def list_pets(self):
        return [p.name for p in self.pets]


class Pet:
    def __init__(self, name: str, age: int, owner: "Owner" = None):
        self.name = name
        self.age = age
        self.owner = owner

    def speak(self):
        """Wird von Unterklassen überschrieben."""
        return "..."

    def info(self):
        return f"{self.name} ({self.age} Jahre)"


class Dog(Pet):
    def __init__(self, name: str, age: int, breed: str, owner: "Owner" = None):
        super().__init__(name, age, owner)
        self.breed = breed

    def speak(self):
        return "Wuff!"


class Cat(Pet):
    def __init__(self, name: str, age: int, color: str, owner: "Owner" = None):
        super().__init__(name, age, owner)
        self.color = color

    def speak(self):
        return "Miau!"

## Beispiel Nutzung:
anna = Owner("Leonie")

rex = Dog("Rex", 4, "Labrador")
hexli = Cat("Hexli", 12, "Tigermuster")

anna.add_pet(rex)
anna.add_pet(hexli)

print(anna.list_pets())   # ['Rex', 'Hexli']
print(rex.speak())        # Wuff!
print(hexli.info())        # Hexli (12 Jahre)