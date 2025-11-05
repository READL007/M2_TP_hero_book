""" Create an adaptator for Guardian to fit Monster interface. """
from ...models.monster import Monster
from ...patterns.bridge.monster_variant import MonsterVariant

#TODO: move class Guardian to models/guardian.py
"""Guardian class representing a Guardian entity in the game.
   A Guardian is similar to a robot
"""
class Guardian:
    """Guardian class representing a Guardian entity in the game."""
    def __init__(self):
        self.name = "Guardian"
        self.power = 100000000000
        self.hp = 1

    def shoot_laser(self) -> str:
        return f"{self.name} shoots a laser with infinite power!"

    def get_stats(self) -> str:
        return f"{self.name} ({self.power}) - HP: {self.hp}"

class GuardianAdaptator(Guardian):
    """Adaptator class to adapt Guardian to Monster interface."""

    def __init__(self):
        self.guardian = Guardian

    def attack(self) -> str:
        return self.guardian.shoot_laser()
