class Tamagotchi:
    """Class representing a Tamagotchi pet."""

    INITIAL_HUNGER = 10
    INITIAL_LIFE = 10

    def __init__(self):
        """Initialize the Tamagotchi with default values."""
        self.hunger = self.INITIAL_HUNGER
        self.life = self.INITIAL_LIFE
        self.invulnerable = True

    def decrease_life(self):
        """Decrease life by 1 point every 2 seconds."""
        if self.life > 0:
            self.life -= 1
            return True
        return False

    def feed(self):
        """Feed the Tamagotchi, reducing hunger and increasing life."""
        if self.hunger > 0:
            self.hunger -= 1
            self.life += 1
            return True
        return False