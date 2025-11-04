"""Base item classes and interfaces."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


class ItemRarity(Enum):
    """Item rarity levels."""
    COMMON = "common"
    RARE = "rare"
    LEGENDARY = "legendary"


@dataclass
class Item(ABC):
    """Abstract base class for all game items."""
    name: str
    rarity: ItemRarity
    
    @abstractmethod
    def use(self) -> str:
        """Use the item and return a description of the effect."""
        pass
    
    def __str__(self) -> str:
        """String representation of the item."""
        return f"[{self.rarity.value}] {self.name}"