"""Room class representing game rooms."""
from dataclasses import dataclass, field
from typing import Dict, List
from .monster import Monster
from .item import Item

@dataclass
class Room:
    """Room class representing game rooms."""
    name: str
    items: List[Item] 
    monsters: List[Monster] 
    connections: Dict[str, "Room"] = field(default_factory=dict)
    
    def connect(self, direction: str, room: "Room") -> None:
        """Connect this room to another room in a given direction."""
        self.connections[direction] = room
    
    def get_details(self) -> str:
        """Get detailed description of the room."""
        details = f"🏰  {self.name}\n"
        if self.items:
            details += "Items in the room:\n"
            for item in self.items:
                details += f" - {item}\n"
        if self.monsters:
            details += "Monsters in the room:\n"
            for monster in self.monsters:
                details += f" - {monster.get_stats()}\n"
        details += "Connections:\n"
        for direction, room in self.connections.items():
            details += f" - {direction}: {room.name}\n"
        return details