class Greet():
    type = "Human"
    def __init__(self, name, species):
        self.firstname = name
        self.species = species
        
    def greet(self):
        print("hello", self.firstname," you are a ", self.species)
    


hum1 = Greet("Randy","mammal")
hum1.greet()

