# class Observable:
#     def __init__(self):
#         self.observers = []

#     def add_observer(self, observer):
#         if observer not in self.observers:
#             self.observers.append(observer)

#     def remove_observer(self, observer):
#         if observer in self.observers:
#             self.observers.remove(observer)

#     def notify_observers(self, *args, **kwargs):
#         for observer in self.observers:
#             observer.update(self, *args, **kwargs)

# class Observer:
#     def update(self, observable, *args, **kwargs):
#         pass

# class Player(Observer): 
#     """Player class representing the game protagonist."""
#     name: str = "Link"
#     health: int = 100
#     inventory: List[Weapon] = field(default_factory=list)

#     def drop_item(self, observable, item: Item) -> None:
#         """Remove a weapon from the player's inventory."""
#         if item in self.inventory:
#             self.inventory.remove(item)

# @dataclass
# class Weapon(Item):
#     """Base weapon class."""
#     damage: int
#     durability: int

#     def use(self) -> str:
#         """Attack with the weapon."""
#         self.durability -= 1
#         if self.durability <= 0:
            
#         enchant_text = f" [{self.enchantment.type.value}]" if self.enchantment else ""
#         return f"⚔️  {self.name}{enchant_text} deals {self.get_total_damage()} damage! (Durability: {self.durability}/{self.get_total_durability()})"
    
# # class WeatherStation(Observable):
# #     def set_temperature(self, temperature):
# #         self.temperature = temperature
# #         self.notify_observers()

# # class PhoneDisplay(Observer):
# #     def update(self, observable, *args, **kwargs):
# #         if isinstance(observable, WeatherStation):
# #             temperature = observable.temperature
# #             print(f"Temperature is {temperature} degrees Celsius")

# # weather_station = WeatherStation()
# # phone_display = PhoneDisplay()

# # weather_station.add_observer(phone_display)
# # weather_station.set_temperature(25)