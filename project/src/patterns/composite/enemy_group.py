#TODO: implement with real monster entity 
class Entity:
    def attack(self): pass

class Monster(Entity):
    def __init__(self, name): self.name = name
    def attack(self): print(f"{self.name} attack !")

class Group(Entity):
    def __init__(self): self.members = []
    def add(self, entity): self.members.append(entity)
    def attack(self):
        for e in self.members:
            e.attack()
