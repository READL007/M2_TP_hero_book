"""Builder pattern for creating complex weapons."""
from typing import Optional, List
from ...models.weapon import Weapon, Sword, Bow, Shield
from ...models.item import ItemRarity
from ...models.enchantment import Enchantment, Gem, EnchantmentType


class WeaponBuilder:
    """Builder for creating complex weapons step by step."""
    
    def __init__(self):
        """Initialize the builder."""
        self._name: Optional[str] = None
        self._damage: int = 10
        self._durability: int = 20
        self._rarity: ItemRarity = ItemRarity.COMMON
        self._enchantment: Optional[Enchantment] = None
        self._gems: List[Gem] = []
        self._special_ability: Optional[str] = None
    
    def set_name(self, name: str) -> 'WeaponBuilder':
        """Set weapon name."""
        self._name = name
        return self
    
    def set_damage(self, damage: int) -> 'WeaponBuilder':
        """Set base damage."""
        self._damage = damage
        return self
    
    def set_durability(self, durability: int) -> 'WeaponBuilder':
        """Set base durability."""
        self._durability = durability
        return self
    
    def set_rarity(self, rarity: ItemRarity) -> 'WeaponBuilder':
        """Set rarity level."""
        self._rarity = rarity
        return self
    
    def add_enchantment(self, enchantment_type: EnchantmentType, power: int) -> 'WeaponBuilder':
        """Add an enchantment to the weapon."""
        self._enchantment = Enchantment(type=enchantment_type, power=power)
        return self
    
    def add_gem(self, gem: Gem) -> 'WeaponBuilder':
        """Add a gem to the weapon."""
        self._gems.append(gem)
        return self
    
    def set_special_ability(self, ability: str) -> 'WeaponBuilder':
        """Set a special ability."""
        self._special_ability = ability
        return self
    
    def build_sword(self) -> Sword:
        """Build a sword with current configuration."""
        if not self._name:
            raise ValueError("Weapon name is required")
        return Sword(
            name=self._name,
            damage=self._damage,
            durability=self._durability,
            rarity=self._rarity,
            enchantment=self._enchantment,
            gems=self._gems.copy(),
            special_ability=self._special_ability
        )
    
    def build_bow(self) -> Bow:
        """Build a bow with current configuration."""
        if not self._name:
            raise ValueError("Weapon name is required")
        return Bow(
            name=self._name,
            damage=self._damage,
            durability=self._durability,
            rarity=self._rarity,
            enchantment=self._enchantment,
            gems=self._gems.copy(),
            special_ability=self._special_ability
        )
    
    def build_shield(self, defense: int) -> Shield:
        """Build a shield with current configuration."""
        if not self._name:
            raise ValueError("Weapon name is required")
        return Shield(
            name=self._name,
            durability=self._durability,
            defense=defense,
            rarity=self._rarity,
            enchantment=self._enchantment,
            gems=self._gems.copy(),
            special_ability=self._special_ability
        )
    
    def reset(self) -> 'WeaponBuilder':
        """Reset the builder to create a new weapon."""
        self.__init__()
        return self


class MasterSwordDirector:
    """Director for building the legendary Master Blade."""
    
    @staticmethod
    def construct(builder: WeaponBuilder) -> Sword:
        """Construct the Master Blade using the builder."""
        ruby = Gem(name="Ruby", bonus_damage=15, bonus_durability=10)
        sapphire = Gem(name="Sapphire", bonus_damage=10, bonus_durability=20)
        
        return (builder
                .set_name("Master Blade")
                .set_damage(50)
                .set_durability(100)
                .set_rarity(ItemRarity.LEGENDARY)
                .add_enchantment(EnchantmentType.LIGHT, 30)
                .add_gem(ruby)
                .add_gem(sapphire)
                .set_special_ability("Shoots beams at full health")
                .build_sword())


class AncientBowDirector:
    """Director for building the Ancient Bow."""
    
    @staticmethod
    def construct(builder: WeaponBuilder) -> Bow:
        """Construct the Ancient Bow using the builder."""
        diamond = Gem(name="Diamond", bonus_damage=20, bonus_durability=15)
        
        return (builder
                .set_name("Ancient Bow of Light")
                .set_damage(40)
                .set_durability(80)
                .set_rarity(ItemRarity.LEGENDARY)
                .add_enchantment(EnchantmentType.LIGHTNING, 25)
                .add_gem(diamond)
                .set_special_ability("Infinite arrows when charged")
                .build_bow())