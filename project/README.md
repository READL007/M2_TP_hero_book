
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
- [x] **Builder** : Weapons (enchtment)
- [x] **Prototype** : Potion
- [x] **Decorator** : Weapon (amalgam)
- [x] **Bridge** : Monster variants
- [x] **Composite** : Monster group
- [ ] Proxy : limit access to item (treasure box protected by key)
- [ ] Adaptator : incorporate incompatible interface to the project
- [ ] Facade :  Use a simplified interface to library
- [ ] Flyweight : Put same monster in cache