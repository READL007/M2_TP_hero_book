"""Monster class using Bridge pattern."""
from game.src.patterns.bridge.monster_variant import MonsterVariant
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Monster(ABC):
    """Abstract Monster class using Bridge pattern."""
    name: str
    variant: MonsterVariant

    def attack(self) -> str:
        return f"{self.name} ({self.variant.color}) attacks with power {self.variant.attack_power()}"

    def get_stats(self) -> str:
        return f"{self.name} ({self.variant.color}) - HP: {self.variant.hp}"
