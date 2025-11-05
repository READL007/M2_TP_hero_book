import copy

class Prototype:
    """Base Prototype class with clone method."""
    def clone(self):
        return copy.deepcopy(self)

class Potion(Prototype):
    def __init__(self, name, effect, potency):
        self.name = name
        self.effect = effect
        self.potency = potency

    def __str__(self):
        return f"Potion(name={self.name}, effect={self.effect}, potency={self.potency})"
    
    def get_full_description(self) -> str:
        """Get detailed weapon description."""
        lines = [
            f"🐑  {self.name}",
            f"   effect: {self.effect}",
            f"   potency:  {self.potency}",
        ]
        return "\n".join(lines)


