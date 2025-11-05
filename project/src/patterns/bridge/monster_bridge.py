""""Monster classes using Bridge pattern.

Monster classes separate the abstraction (Monster) from its implementation (MonsterVariant).

Thanks to this pattern, we can create different monster types with various variants without creating a complex inheritance hierarchy.

Without bridge pattern, we would need to create a class for each combination of monster type and variant, leading to a combinatorial explosion of classes.

"""
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
