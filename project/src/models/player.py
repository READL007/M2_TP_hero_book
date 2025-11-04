"""Player class representing the game protagonist."""

from dataclasses import dataclass, field
from typing import List
from .weapon import Weapon

@dataclass
class Player:
    """Player class representing the game protagonist."""
    name: str = "Link"
    health: int = 100
    inventory: List[Weapon] = field(default_factory=list)
    
    def attack(self, weapon: Weapon) -> str:
        """Player attacks using a specified weapon."""
        if weapon in self.inventory:
            return weapon.use()
        return f"{self.name} does not have {weapon.name} in inventory."
    
    def pick_weapon(self, weapon: Weapon) -> None:
        """Add a weapon to the player's inventory."""
        self.inventory.append(weapon)
    
    def get_status(self) -> str:
        """Get current status of the player."""
        return f"Player: {self.name}, Health: {self.health}, Mana: {self.mana}, Weapons: {[w.name for w in self.inventory]}"