 # Demo patterns

from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from ..models.player import Player

from .bridge.monster_bridge import Bokoblin, Moblin
from .bridge.monster_variant import BlueVariant, RedVariant
from .factory.item_factory import CommonItemFactory, RareItemFactory, LegendaryItemFactory, WeaponFactory
from .builder.weapon_builder import WeaponBuilder, MasterSwordDirector, AncientBowDirector
from ..models.item import ItemRarity
from ..models.enchantment import EnchantmentType, Gem
from .prototype.potion_prototype import Potion

class Demo :
    def __init__(self) -> None:
        self.console = Console()

    """Class to demonstrate various design patterns."""
    def call_demo(self) -> None:
        """Call all pattern demos."""    
        self._demo_factories()
        self.console.print("\n")
        self._demo_builders()
        self.console.print("\n")
        self._demo_prototype()
        self.console.print("\n")
        self._demo_bridge()
    
    def _demo_factories(self) -> None:
        """Demonstrate factory patterns."""
        self.console.print("[bold yellow]📦 Factory Pattern Demo[/bold yellow]\n")
        
        # Abstract Factory demo
        common_factory = CommonItemFactory()
        legendary_factory = LegendaryItemFactory()
        
        common_weapon = common_factory.create_weapon()
        legendary_weapon = legendary_factory.create_weapon()
        
        # Display items
        table = Table(title="Factory-Created Items", border_style="cyan")
        table.add_column("Item", style="bold")
        table.add_column("Action", style="green")
        
        table.add_row(str(common_weapon), common_weapon.use())
        table.add_row(str(legendary_weapon), legendary_weapon.use())
        
        self.console.print(table)
    
    def _demo_builders(self) -> None:
        """Demonstrate builder pattern."""
        self.console.print("[bold yellow]🏗️  Builder Pattern Demo[/bold yellow]\n")
        
        builder = WeaponBuilder()
        
        # Using Director for Master Blade
        master_blade = MasterSwordDirector.construct(builder)
        
        # Using Director for Ancient Bow
        builder.reset()
        ancient_bow = AncientBowDirector.construct(builder)
        
        # Custom weapon using builder directly
        builder.reset()
        custom_sword = (builder
                       .set_name("Flame Sword of the Hero")
                       .set_damage(35)
                       .set_durability(60)
                       .set_rarity(ItemRarity.RARE)
                       .add_enchantment(EnchantmentType.FIRE, 20)
                       .add_gem(Gem("Topaz", bonus_damage=8, bonus_durability=5))
                       .set_special_ability("Burns enemies on hit")
                       .build_sword())
        
        # Display weapons
        self.console.print(Panel(master_blade.get_full_description(), title="Legendary Weapon", border_style="yellow"))
        self.console.print(Panel(ancient_bow.get_full_description(), title="Ancient Weapon", border_style="blue"))
        self.console.print(Panel(custom_sword.get_full_description(), title="Custom Weapon", border_style="red"))
        
    def _demo_prototype(self) -> None:
        """Demonstrate prototype pattern."""
        # Create an original potion prototype
        healing_potion = Potion("Healing Potion", "heal", 50)

        # Clone the potion for the player
        player_potion = healing_potion.clone()
        player_potion.name = "Player's Healing Potion"

        self.console.print("[bold yellow]🧑‍🤝‍🧑  Prototype  Pattern Demo[/bold yellow]\n")
        self.console.print(Panel(healing_potion.get_full_description(), title="Original", border_style="yellow"))
        self.console.print(Panel(player_potion.get_full_description(), title="Copy", border_style="yellow"))

    def _demo_bridge(self) -> None:
        """Demonstrate bridge pattern."""
        red_variant = RedVariant()
        blue_variant = BlueVariant()

        bokoblin_red = Bokoblin(red_variant)
        moblin_blue = Moblin(blue_variant)

        self.console.print(bokoblin_red.attack())
        self.console.print(moblin_blue.get_stats())