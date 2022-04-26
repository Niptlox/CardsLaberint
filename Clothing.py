from Statistic import Level_system, Statistic_clothing
import Items



class Clothing(Items.Item):
    def __init__(self, name, cost=0, statistic=Statistic_clothing(), lvl=Level_system(), images={}, item_type=Items.TYPE_CLOTHING):
        super().__init__(name, cost, images, item_type)
        self.statistic = statistic
        self.lvl = lvl

    def dress(self, owner):
        if owner.lvl >= self.lvl:
            return True
        else:
            return False
