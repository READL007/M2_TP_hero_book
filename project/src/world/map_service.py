"""Service to build a world"""
from ..models.room import Room
from ..models.monster import Monster
from ..models.item import Item
from ..patterns.bridge.monster_variant import RedVariant, BlueVariant
from ..patterns.bridge.monster_bridge import Bokoblin, Moblin
from ..patterns.factory.item_factory import CommonItemFactory, RareItemFactory, LegendaryItemFactory, WeaponFactory

class MapService:
    """Service class for building and managing a map of rooms with monsters and items."""

    @staticmethod
    def build_world() -> None:
        """Build the game world with rooms, monsters, and items."""

        #TODO: replace with factory pattern to create room  
        room1 = Room(
            name="Ancient Forest",
            items=[],
            monsters=[]
            )
        room2 = Room(
            name="Dark Cave",
            items=[],
            monsters=[]
            )
        room3 = Room(
            name="Abandoned Hyrule Castle",
            items=[],
            monsters=[]
            )
        # create room connectioins
        room1.connect("north", room2)
        room2.connect("south", room1)
        room2.connect("east", room3)
        room3.connect("west", room2)

        # TODO: maybe CoR pattern can help us create our world instead of doing it manually?
        # populate rooms with monsters and items
        # TODO: have a treasur box in last room that can only be opened with a key
        room1.items.append(CommonItemFactory().create_weapon())
        room1.items.append(CommonItemFactory().create_key())

        room2.items.append(RareItemFactory().create_potion())
        room2.monsters.append(Bokoblin(RedVariant()))
        
        room3.items.append(RareItemFactory().create_weapon())
        room3.monsters.append(Moblin(BlueVariant()))

        return [room1, room2, room3]


