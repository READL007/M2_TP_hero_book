"""Factory and Abstract Factory patterns for item creation.

This module implements both the Factory Method and Abstract Factory patterns:

1. Abstract Factory (ItemFactory): Creates families of related items (weapons and potions)
   of different rarities (Common, Rare, Legendary)
2. Factory Method (WeaponFactory): Creates specific types of weapons
"""
from abc import ABC, abstractmethod
from typing import Type
from ...models.item import Item, ItemRarity
from ...models.weapon import Weapon, Sword, Bow, Shield
from ...models.potion import Potion, PotionEffect
from ...models.key import Key


class ItemFactory(ABC):
    """Abstract Factory for creating items.
    
    This is the abstract base class that defines the interface for creating
    families of related items. Each concrete factory will create items of
    a specific rarity level (Common, Rare, Legendary).
    """
    
    @abstractmethod
    def create_weapon(self) -> Weapon:
        """Create a weapon."""
        pass
    
    @abstractmethod
    def create_potion(self) -> Potion:
        """Create a potion."""
        pass


class CommonItemFactory(ItemFactory):
    """Factory for common items.
    
    Creates low-tier items suitable for beginning players:
    - Weapons: Basic weapons with low damage and durability
    - Potions: Basic healing potions with minimal effects
    - Key : Basic key what could it open?
    """
    
    def create_weapon(self) -> Weapon:
        """Create a common weapon (random sword)."""
        return Sword(
            name="Traveler's Sword",
            damage=5,
            durability=20,
            rarity=ItemRarity.COMMON
        )
    
    def create_potion(self) -> Potion:
        """Create a common potion."""
        return Potion(
            name="Red Potion",
            rarity=ItemRarity.COMMON,
            effect=PotionEffect.HEAL,
            power=20
        )
    
    def create_key(self) -> Key:
        """Create a common key."""
        return Key(
            name="Old Key",
            rarity=ItemRarity.COMMON,
        )


class RareItemFactory(ItemFactory):
    """Factory for rare items."""
    
    def create_weapon(self) -> Weapon:
        """Create a rare weapon."""
        return Bow(
            name="Royal Bow",
            damage=15,
            durability=35,
            rarity=ItemRarity.RARE
        )
    
    def create_potion(self) -> Potion:
        """Create a rare potion."""
        return Potion(
            name="Elixir of Strength",
            rarity=ItemRarity.RARE,
            effect=PotionEffect.STRENGTH,
            power=50
        )
    
    def create_key(self) -> Key:
        """Create a rare key."""
        return Key(
            name="Silver Key",
            rarity=ItemRarity.RARE,
        )



class LegendaryItemFactory(ItemFactory):
    """Factory for legendary items."""
    
    def create_weapon(self) -> Weapon:
        """Create a legendary weapon."""
        return Sword(
            name="Master Blade",
            damage=50,
            durability=100,
            rarity=ItemRarity.LEGENDARY
        )
    
    def create_potion(self) -> Potion:
        """Create a legendary potion."""
        return Potion(
            name="Goddess Tear",
            rarity=ItemRarity.LEGENDARY,
            effect=PotionEffect.HEAL,
            power=999
        )
    
    def create_key(self) -> Key:
        """Create a legandary key."""
        return Key(
            name="Master Key",
            rarity=ItemRarity.LEGENDARY,
        )


class WeaponFactory:
    """Factory Method for creating specific weapon types."""
    
    @staticmethod
    def create_weapon(weapon_class: Type[Weapon], name: str, **kwargs) -> Weapon:
        """Create a weapon of the specified type."""
        return weapon_class(name=name, **kwargs)
    
    @staticmethod
    def create_sword(name: str, damage: int, durability: int, rarity: ItemRarity) -> Sword:
        """Create a sword."""
        return Sword(name=name, damage=damage, durability=durability, rarity=rarity)
    
    @staticmethod
    def create_bow(name: str, damage: int, durability: int, rarity: ItemRarity) -> Bow:
        """Create a bow."""
        return Bow(name=name, damage=damage, durability=durability, rarity=rarity)
    
    @staticmethod
    def create_shield(name: str, durability: int, defense: int, rarity: ItemRarity) -> Shield:
        """Create a shield."""
        return Shield(name=name, durability=durability, defense=defense, rarity=rarity)