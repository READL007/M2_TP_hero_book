"""Builder pattern for creating complex map with rooms."""
from typing import List, Optional
from ...models.room import Room
from ...models.monster import Monster
from ...models.item import Item

class MapBuilder:
    """Builder for creating complex map with rooms step by step."""
    
    def __init__(self):
        """Initialize the builder."""
        self._rooms: List[Room] = []
    
    def add_room(self, room: Room) -> 'MapBuilder':
        """Add a room to the map."""
        self._rooms.append(room)
        return self
    
    def connect_rooms(self, room1: Room, direction: str, room2: Room) -> 'MapBuilder':
        """Connect two rooms in a given direction."""
        room1.connect(direction, room2)
        return self
    
    def build(self) -> List[Room]:
        """Build and return the list of rooms in the map."""
        return self._rooms