class character:
    def __init__(self, name):
        self.name = name
    def walk(self):
        print(f"{self.name} chal raha hai.")
class wizard(character):
    
    
    def walk(self):
        print(f"{self.name} chalta nahi hai, wo teleport ho jaata hai.")
    def cast_spell(self):
        print(f"{self.name} using his powers!!")
p1 = character("Sameer")
p2 = wizard("Doctor Strange")
p1.walk()
p2.walk()
