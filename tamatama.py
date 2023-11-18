import pygame
import tkinter as tk
import time

from tkinter import ttk

# Define la clase Tamagotchi
class Tamagotchi:
    def __init__(self):
        # Inicializa el nivel de hambre en 10
        self.hunger = 10
        self.life = 10
        self.invulnerable = True

    def decrease_life(self):
        if self.life > 0:
            self.life -= 1
            return True
        return False

    def feed(self):
        # Si el Tamagotchi tiene hambre, reduce el nivel de hambre en 1 y devuelve True
        if self.hunger > 0:
            self.hunger -= 1
            self.life += 1
            return True
        # Si el Tamagotchi no tiene hambre, devuelve False
        return False

# Define la clase de la aplicación
class Application(tk.Tk):
    def __init__(self, tamagotchi):
        # Inicializa la aplicación
        tk.Tk.__init__(self)
        self.tamagotchi = tamagotchi


        # Initialize the pygame mixer
        pygame.mixer.init()


        # Load the sound effects
        self.feed_sound = pygame.mixer.Sound('sounds/feed_sound.wav')
        self.death_sound = pygame.mixer.Sound('sounds/death_sound.wav')

        # Crea una etiqueta para mostrar el arte ASCII de Totoro
        self.character_label = tk.Label(self, text=
        """
        ^ - ^
        ( o o )
        U   J
        """)
        self.character_label.pack()

        # Crea una barra de vida para el Tamagotchi
        self.life_bar = ttk.Progressbar(self, length=100, mode='determinate', maximum=10)
        self.life_bar.pack()
        self.life_bar['value'] = self.tamagotchi.life

        # Crea una etiqueta para mostrar el nivel de hambre del Tamagotchi
        self.hunger_label = tk.Label(self, text=f"Hunger: {self.tamagotchi.hunger}")
        self.hunger_label.pack()

        # Crea un botón para alimentar al Tamagotchi
        self.feed_button = tk.Button(self, text="Feed", command=self.feed_tamagotchi)
        self.feed_button.pack()

        # Actualiza la etiqueta de hambre
        self.update_hunger_label()

    def feed_tamagotchi(self):
        # Alimenta al Tamagotchi y cambia el arte ASCII a una versión feliz si el Tamagotchi tiene hambre
        if self.tamagotchi.feed():
            self.character_label.config(text=
            """
            ^ - ^
            ( ^ ^ )
            U   J
            """)
            # Después de 1 segundo, resetea el arte ASCII a la versión normal
            self.after(1000, self.reset_tamagotchi)
            self.feed_sound.play()

        # Actualiza la etiqueta de hambre
        self.update_hunger_label()

    def reset_tamagotchi(self):
        # Resetea el arte ASCII a la versión normal
        self.character_label.config(text=
        """
        ^ - ^
        ( o o )
        U   J
        """)

    def update_hunger_label(self):
        # Actualiza la etiqueta de hambre cada segundo
        self.hunger_label.config(text=f"Hunger: {self.tamagotchi.hunger}")
        self.after(1000, self.update_hunger_label)

    def update_life_bar(self):
        # Disminuye la vida del Tamagotchi cada 2 segundos
        if self.tamagotchi.decrease_life():
            self.life_bar['value'] = self.tamagotchi.life
        else:
            # Si la vida del Tamagotchi llega a 0, muestra la animación de muerte
            self.character_label.config(text=
            """
            x - x
            ( x x )
            U   J
            """)
        self.after(2000, self.update_life_bar)
        self.death_sound.play()


if __name__ == "__main__":
    # Crea una instancia de Tamagotchi
    my_tamagotchi = Tamagotchi()

    # Crea una instancia de la aplicación con el Tamagotchi
    app = Application(my_tamagotchi)

    # Ejecuta la aplicación
    app.update_life_bar()
    app.mainloop()