"""Base item classes and interfaces."""
from dataclasses import dataclass
from enum import Enum
from .item import Item, ItemRarity


@dataclass
class Key(Item):
    """Key item"""
    name: str
    rarity: ItemRarity
    
    def use(self) -> str:
        """Use the item and return a description of the effect."""
        return f"✨ What can this {self.name} do ?"
    
