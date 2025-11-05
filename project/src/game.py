"""Singleton Game - manages global game state."""
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from typing import List

from .models.player import Player
from .patterns.demo import Demo
from .world.map_service import MapService
from .models.room import Room

class Game:
    """Singleton Game class managing global game state."""
    #Singleton representing the current game session.
    # private instance that stores the single Game instance
    _instance: Optional["Game"] = None
    world: List[Room] = []
    
    # private constructor that checks if an instance already exists
    # and redirect to use get_instance() method 
    def __init__(self) -> None:
        """Initialize the game (do not call directly init)."""
        if Game._instance is not None:
            raise RuntimeError("Use Game.get_instance() to get the instance.")
        self.console = Console()
        self.player = Player()
        #self.map = 
            
    # decorated with @classmethod which means it can be called on the class itself
    # implements the Singleton pattern
    # if no instance exists, create one and store it in _instance
    # else return the existing instance
    @classmethod
    def get_instance(cls) -> "Game":
        """Return the unique game instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def start(self) -> None:
        """Start the game with main menu."""
        self.console.print(Panel.fit(
            "[bold cyan]🗡️  HYRULE LEGEND  🗡️[/bold cyan]\n"
            "[dim]A Design Patterns Adventure[/dim]",
            border_style="green"
        ))
        
        choice = Prompt.ask(
            "\n[yellow]Menu[/yellow]",
            choices=["start", "quit"],
            default="start"
        )
        
        if choice == "start":
            self._start_game()
        else:
            self.console.print("[red]Farewell, hero![/red]")
    
    def _start_game(self) -> None:
        """Initialize and run the game loop."""
        self.is_running = True
        self.console.print(f"\n[green]Welcome, {self.player.name}![/green]\n")
        # demo = Demo()
        # demo.call_demo()
        # TODO: Implement a facade for game with world building and interactions
        self.world = MapService.build_world()
        self.console.print("[bold magenta]Your adventure begins now...[/bold magenta]")
        self.console.print(f"[dim]You find yourself in the {self.world[0].name}.[/dim]")
        self.console.print(self.world[0].get_details())
        
       
        
    
