
## Installation
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run Game
```bash
python main.py
```

## Implemented Patterns:

- [x] **Singleton** : Game
- [x] **Factory/Abstract Factory** : Items/Weapons
- [x] **Builder** : Weapons (enchantment)
- [x] **Prototype** : Potion
- [x] **Decorator** : Weapon (amalgam)
- [x] **Bridge** : Monster variants
- [x] **Composite** : Monster group
- [x] **Proxy** : limit access to item (treasure box protected by key)
- [x] **Adaptator** : incorporate incompatible interface to the project ex gardian need to adapt monster
- [ ] Facade : Use a simplified interface to library
- [ ] Flyweight : Put same monster in cache
- [ ] CoR :
- [ ] Command :
- [ ] Iterator :
- [ ] Mediator :
- [ ] Memento :
- [ ] Observer : Watch WeaponBrokenState and drop from inventory
- [x] **State** : Weapon is broken or not (WeaponBrokenState)
- [ ] Strategy :
- [ ] Template :
- [ ] Visitor :

