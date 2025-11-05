"""Implementation of the Proxy Pattern for treasure boxes in the game.

This could be directly integrated into the Item class hierarchy, but is separated here
for demonstrating the Proxy pattern.
"""

class TreasureProxy:
    """Proxy class for a treasure box that requires a key to open."""
    def __init__(self, treasure: str, required_key: str) -> None:
        self._treasure = treasure
        self._required_key = required_key
        self._is_opened = False
    
    def open(self, player_inventory: list) -> str:
        """Attempt to open the treasure box with the player's keys."""
        if self._is_opened:
            return "The treasure box is already opened."
        
        if self._required_key in player_inventory:
            self._is_opened = True
            return f"You opened the treasure box and found: {self._treasure}"
        else:
            return "You need a key to open this treasure box."
