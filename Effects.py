class Effect():
    def __init__(self, name, rounds=1, lvl=1, max_lvl=5):
        self.name = name
        self.rounds = rounds
        self.lvl = lvl
        self.max_lvl = max_lvl

    def update(self, entity):
        pass

class Regeneration(Effect):
    def __init__(self, lvl=1):
        rounds = int((i / 4.5) + i ** 0.3 * 2)
        # rounds [2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 11, 11]
        self.super("regen", rounds, lvl, 5)
        self.regen = int((i // 3) + i ** 0.9) + 1
        # regen [2, 2, 4, 5, 6, 8, 8, 9, 11, 11, 12, 14, 15, 15, 17, 18, 18, 20, 21, 21, 23, 24, 24, 26, 27, 27, 29, 30, 30]

    def update(self, entity):
        self.add_hp(self.regen)
        self.rounds -= 1
        return self.rounds > 0
