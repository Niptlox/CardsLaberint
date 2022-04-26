import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import Entitys as Ent
import Field as Fd
import Player as Pr
from Field_creater import load_map


class Game:
    def __init__(self):
        self.field = load_map("Laberint Oratori")
        self.player = Pr.Player()
        self.player.set_room(self.field.get_entry_room)
        print(self.field.field)

    




if __name__ == "__main__":
    game = Game()
