"""Potion types and classes."""
from dataclasses import dataclass
from enum import Enum
from .item import Item, ItemRarity


class PotionEffect(Enum):
    """Types of potion effects."""
    HEAL = "heal"
    STAMINA = "stamina"
    STRENGTH = "strength"


@dataclass
class Potion(Item):
    """Potion consumable item."""
    effect: PotionEffect
    power: int
    
    def use(self) -> str:
        """Consume the potion."""
        return f"✨ {self.name} restores {self.power} {self.effect.value}!"