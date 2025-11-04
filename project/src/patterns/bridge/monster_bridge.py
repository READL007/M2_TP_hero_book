""""Monster classes using Bridge pattern."""
from .monster_variant import MonsterVariant

class Monster:
    def __init__(self, name: str, variant: MonsterVariant):
        self.name = name
        self.variant = variant

    def attack(self):
        return f"{self.name} ({self.variant.color}) attacks with {self.variant.attack_power()} points !"

    def get_stats(self):
        return f"{self.name} ({self.variant.color}) - HP: {self.variant.hp()}"

class Bokoblin(Monster):
    def __init__(self, variant: MonsterVariant):
        super().__init__("Bokoblin", variant)

class Moblin(Monster):
    def __init__(self, variant: MonsterVariant):
        super().__init__("Moblin", variant)

class Hinox(Monster):
    def __init__(self, variant: MonsterVariant):
        super().__init__("Hinox", variant)
