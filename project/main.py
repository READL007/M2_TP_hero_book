"""Entry point for the Zelda-like game."""
from src.game import Game


def main() -> None:
    """Launch a game session."""
    """This implements the Singleton pattern for the Game class."""
    # We call get_instance() to ensure only one instance is created instead of calling the constructor directly
    # it ensures there is only one Game state and provides a global access point to it
    game = Game.get_instance()
    # game1 = Game.get_instance()
    # game2 = Game.get_instance()
    # print(game1 is game2) 
    game.start()


if __name__ == "__main__":
    main()