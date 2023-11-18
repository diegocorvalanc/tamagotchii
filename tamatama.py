import pygame
import tkinter as tk
import time

from tkinter import ttk


class Tamagotchi:
    def __init__(self):
        # Initializes the hunger level at 10
        self.hunger = 10
        self.life = 10
        self.invulnerable = True

    def decrease_life(self):
        # Decrese life in 1 point each 2 seconds
        if self.life > 0:
            self.life -= 1
            return True
        return False

    def feed(self):
        # If Tamagotchi is hungry, it reduces the hunger level by 1
        if self.hunger > 0:
            self.hunger -= 1
            self.life += 1
            return True
        return False


class Application(tk.Tk):
    def __init__(self, tamagotchi):
        tk.Tk.__init__(self)
        self.tamagotchi = tamagotchi


        # Initialize the pygame mixer
        pygame.mixer.init()


        # Load the sound effects
        self.feed_sound = pygame.mixer.Sound('sounds/feed_sound.wav')
        self.death_sound = pygame.mixer.Sound('sounds/death_sound.wav')

        # Normal Tamatama
        self.character_label = tk.Label(self, text=
        """
        ^ - ^
        ( o o )
        U   J
        """)
        self.character_label.pack()

        # Tamatama life bar
        self.life_bar = ttk.Progressbar(self, length=100, mode='determinate', maximum=10)
        self.life_bar.pack()
        self.life_bar['value'] = self.tamagotchi.life

        # Tamatama hunger label
        self.hunger_label = tk.Label(self, text=f"Hunger: {self.tamagotchi.hunger}")
        self.hunger_label.pack()

        # Feed Tamatama
        self.feed_button = tk.Button(self, text="Feed", command=self.feed_tamagotchi)
        self.feed_button.pack()

        # Update the hunger label every second
        self.update_hunger_label()

    def feed_tamagotchi(self):
        # Happy Tamatama
        if self.tamagotchi.feed():
            self.character_label.config(text=
            """
            ^ - ^
            ( ^ ^ )
            U   J
            """)
            self.after(1000, self.reset_tamagotchi)
            self.feed_sound.play()

        # Actualiza la etiqueta de hambre
        self.update_hunger_label()

    def reset_tamagotchi(self):
        self.character_label.config(text=
        """
        ^ - ^
        ( o o )
        U   J
        """)

    def update_hunger_label(self):
        # Update hunger label every second
        self.hunger_label.config(text=f"Hunger: {self.tamagotchi.hunger}")
        self.after(1000, self.update_hunger_label)

    def update_life_bar(self):
        # Decrease life bar every 2 seconds
        if self.tamagotchi.decrease_life():
            self.life_bar['value'] = self.tamagotchi.life
        else:
            # Sadly Tamatama it's d word
            self.character_label.config(text=
            """
            ^ - ^
            ( x x )
            U   J
            """)
        self.after(2000, self.update_life_bar)
        self.death_sound.play()


if __name__ == "__main__":
    my_tamagotchi = Tamagotchi()

    app = Application(my_tamagotchi)

    # Exec
    app.update_life_bar()
    app.mainloop()