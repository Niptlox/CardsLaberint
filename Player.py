import Entitys as En

class Player(En.Entity):
    pass
    def __init__(self, name="Player"):
        statistic_combat = En.Statistic_combat(max_hp = 15, max_ap=10, max_mp=10,
                                            attack_power=3, crit_attac_mult=1,
                                            attack_p=5, move_p=0, change_p=6, item_use_p=6,
                                            attac_c=60, crit_attac_c=0, block_c=5,
                                            attac_effects=[], my_effects=[])
        super().__init__(name, statistic_combat, money=0, xp=0, enemy=False,
                         inventory=[], dressed_items=[], xy=(0, 0), room=None)
