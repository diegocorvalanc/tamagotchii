from src.tamagotchi import Tamagotchi
from src.application import Application

if __name__ == "__main__":
    my_tamagotchi = Tamagotchi()
    app = Application(my_tamagotchi)

    # Execute
    app.update_life_bar()
    app.mainloop()