"""Weapon types and classes."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List
from .item import Item, ItemRarity
from .enchantment import Enchantment, Gem


class WeaponType(Enum):
    """Types of weapons available."""
    SWORD = "sword"
    BOW = "bow"
    SHIELD = "shield"


@dataclass
class Weapon(Item):
    """Base weapon class."""
    damage: int
    durability: int
    weapon_type: WeaponType
    enchantment: Optional[Enchantment] = None
    gems: List[Gem] = field(default_factory=list)
    special_ability: Optional[str] = None
    
    def get_total_damage(self) -> int:
        """Calculate total damage including bonuses."""
        total = self.damage
        if self.enchantment:
            total += self.enchantment.power
        for gem in self.gems:
            total += gem.bonus_damage
        return total
    
    def get_total_durability(self) -> int:
        """Calculate total durability including bonuses."""
        total = self.durability
        for gem in self.gems:
            total += gem.bonus_durability
        return total
    
    def use(self) -> str:
        """Attack with the weapon."""
        self.durability -= 1
        enchant_text = f" [{self.enchantment.type.value}]" if self.enchantment else ""
        return f"⚔️  {self.name}{enchant_text} deals {self.get_total_damage()} damage! (Durability: {self.durability}/{self.get_total_durability()})"
    
    def is_broken(self) -> bool:
        """Check if weapon is broken."""
        return self.durability <= 0
    
    def get_full_description(self) -> str:
        """Get detailed weapon description."""
        lines = [
            f"🗡️  {self.name}",
            f"   Rarity: {self.rarity.value}",
            f"   Damage: {self.get_total_damage()} (Base: {self.damage})",
            f"   Durability: {self.get_total_durability()}"
        ]
        
        if self.enchantment:
            lines.append(f"   ✨ {self.enchantment.get_description()}")
        
        if self.gems:
            lines.append(f"   💎 Gems:")
            for gem in self.gems:
                lines.append(f"      • {gem.get_description()}")
        
        if self.special_ability:
            lines.append(f"   🌟 Special: {self.special_ability}")
        
        return "\n".join(lines)


@dataclass
class Sword(Weapon):
    """Sword weapon type."""
    
    def __init__(
        self,
        name: str,
        damage: int,
        durability: int,
        rarity: ItemRarity,
        enchantment: Optional[Enchantment] = None,
        gems: Optional[List[Gem]] = None,
        special_ability: Optional[str] = None
    ):
        super().__init__(
            name=name,
            rarity=rarity,
            damage=damage,
            durability=durability,
            weapon_type=WeaponType.SWORD,
            enchantment=enchantment,
            gems=gems or [],
            special_ability=special_ability
        )


@dataclass
class Bow(Weapon):
    """Bow weapon type."""
    arrow_count: int = 30
    
    def __init__(
        self,
        name: str,
        damage: int,
        durability: int,
        rarity: ItemRarity,
        enchantment: Optional[Enchantment] = None,
        gems: Optional[List[Gem]] = None,
        special_ability: Optional[str] = None
    ):
        super().__init__(
            name=name,
            rarity=rarity,
            damage=damage,
            durability=durability,
            weapon_type=WeaponType.BOW,
            enchantment=enchantment,
            gems=gems or [],
            special_ability=special_ability
        )
    
    def use(self) -> str:
        """Shoot an arrow."""
        if self.arrow_count <= 0:
            return f"🏹 {self.name} has no arrows left!"
        self.arrow_count -= 1
        self.durability -= 1
        enchant_text = f" [{self.enchantment.type.value}]" if self.enchantment else ""
        return f"🏹 {self.name}{enchant_text} shoots! {self.get_total_damage()} damage. (Arrows: {self.arrow_count})"


@dataclass
class Shield(Weapon):
    """Shield weapon type."""
    defense: int = 0
    
    def __init__(
        self,
        name: str,
        durability: int,
        defense: int,
        rarity: ItemRarity,
        enchantment: Optional[Enchantment] = None,
        gems: Optional[List[Gem]] = None,
        special_ability: Optional[str] = None
    ):
        super().__init__(
            name=name,
            rarity=rarity,
            damage=0,
            durability=durability,
            weapon_type=WeaponType.SHIELD,
            enchantment=enchantment,
            gems=gems or [],
            special_ability=special_ability
        )
        self.defense = defense
    
    def use(self) -> str:
        """Block with the shield."""
        self.durability -= 1
        return f"🛡️  {self.name} blocks! (Defense: {self.defense}, Durability: {self.durability})"