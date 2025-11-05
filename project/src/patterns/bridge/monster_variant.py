from abc import ABC, abstractmethod
"""Monster variant implementations for Bridge pattern.

Each variant defines specific attributes and behaviors for monsters.
They are more or less powerfull and resistant depending on their color.
"""
class MonsterVariant(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def hp(self) -> int: ...
    @abstractmethod
    def attack_power(self) -> int: ...

class RedVariant(MonsterVariant):
    def __init__(self): super().__init__("red")
    def hp(self): return 50
    def attack_power(self): return 10

class BlueVariant(MonsterVariant):
    def __init__(self): super().__init__("blue")
    def hp(self): return 15
    def attack_power(self): return 50

class WhiteVariant(MonsterVariant):
    def __init__(self): super().__init__("white")
    def hp(self): return 120
    def attack_power(self): return 25
