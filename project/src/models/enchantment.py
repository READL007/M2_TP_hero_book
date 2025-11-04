"""Enchantments and special properties for weapons."""
from dataclasses import dataclass
from enum import Enum


class EnchantmentType(Enum):
    """Types of enchantments."""
    FIRE = "fire"
    ICE = "ice"
    LIGHTNING = "lightning"
    LIGHT = "light"
    DARKNESS = "darkness"


@dataclass
class Enchantment:
    """Enchantment that can be applied to weapons."""
    type: EnchantmentType
    power: int
    
    def get_description(self) -> str:
        """Get enchantment description."""
        return f"[{self.type.value.upper()}] +{self.power} elemental damage"


@dataclass
class Gem:
    """Gem that can be socketed into weapons."""
    name: str
    bonus_damage: int
    bonus_durability: int
    
    def get_description(self) -> str:
        """Get gem description."""
        return f"{self.name} (+{self.bonus_damage} DMG, +{self.bonus_durability} DUR)"