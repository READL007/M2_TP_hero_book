class Weapon:
    def attack(self):
        return 10

class WeaponDecorator(Weapon):
    def __init__(self, weapon):
        self.weapon = weapon

class RockFusion(WeaponDecorator):
    def attack(self):
        return self.weapon.attack() + 5

class WoodFusion(WeaponDecorator):
    def attack(self):
        return self.weapon.attack() + 3

weapon = RockFusion(WoodFusion(Weapon()))
print(weapon.attack())  
