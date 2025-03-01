import pygame
import tkinter as tk
from tkinter import ttk
from src.tamagotchi import Tamagotchi

UPDATE_HUNGER_INTERVAL = 1000  # milliseconds
UPDATE_LIFE_INTERVAL = 2000  # milliseconds


class Application(tk.Tk):
    """Class representing the Tamagotchi application."""

    def __init__(self, tamagotchi):
        """Initialize the application with a Tamagotchi instance."""
        super().__init__()
        self.tamagotchi = tamagotchi
        self.title("Tamagotchi experiment")

        # Initialize the pygame mixer
        pygame.mixer.init()

        self.character_name = ttk.Label(self, text="Tamatama")
        self.character_name.pack()

        # Load the sound effects
        self.feed_sound = pygame.mixer.Sound("sounds/feed_sound.wav")
        self.death_sound = pygame.mixer.Sound("sounds/death_sound.wav")

        self.character_label = tk.Label(
            self,
            text="""
        ^ - ^
        ( o o )
        U   J
        """,
        )
        self.character_label.pack()

        # Tamatama life bar
        self.life_bar = ttk.Progressbar(
            self, length=100, mode="determinate", maximum=Tamagotchi.INITIAL_LIFE
        )
        self.life_bar.pack()
        self.life_bar["value"] = self.tamagotchi.life

        # Tamatama hunger label
        self.hunger_label = tk.Label(self, text=f"Hunger: {self.tamagotchi.hunger}")
        self.hunger_label.pack()

        # Feed Tamatama
        self.feed_button = tk.Button(self, text="Feed", command=self.feed_tamagotchi)
        self.feed_button.pack()

        # Update the hunger label every second
        self.update_hunger_label()

    def feed_tamagotchi(self):
        """Feed the Tamagotchi and update the UI."""
        if self.tamagotchi.feed():
            self.character_label.config(
                text="""
            ^ - ^
            ( ^ ^ )
            U   J
            """
            )
            self.after(1000, self.reset_tamagotchi)
            self.feed_sound.play()

        self.update_hunger_label()

    def reset_tamagotchi(self):
        """Reset the Tamagotchi character label."""
        self.character_label.config(
            text="""
        ^ - ^
        ( o o )
        U   J
        """
        )

    def update_hunger_label(self):
        """Update the hunger label every second."""
        self.hunger_label.config(text=f"Hunger: {self.tamagotchi.hunger}")
        self.after(UPDATE_HUNGER_INTERVAL, self.update_hunger_label)

    def update_life_bar(self):
        """Update the life bar every 2 seconds."""
        if self.tamagotchi.decrease_life():
            self.life_bar["value"] = self.tamagotchi.life
        else:
            self.character_label.config(
                text="""
            ^ - ^
            ( x x )
            U   J
            """
            )
            self.death_sound.play()
        self.after(UPDATE_LIFE_INTERVAL, self.update_life_bar)