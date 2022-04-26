import Clothing as Cl


class Weapon(Cl.Clothing):
    item_type = "weapon"
    def __init__(self, name, cost=0, statistic=Cl.Statistic_clothing(), lvl=Cl.Level_system(), images={}, item_type=Cl.Items.TYPE_WEAPON):
        super().__init__(name, cost, statistic, lvl, images=images, item_type=item_type)

class Sword_1(Weapon):
    def __init__(self):
        super().__init__("Sword", cost=140, statistic=Cl.Statistic_clothing(attack_power=(1,2), attack_p=5), lvl=Cl.Level_system(lvl_sword=1))

def create_class_item(name, cost=0, statistic=Cl.Statistic_clothing(), lvl=Cl.Level_system(), images={}):
    return lambda: Cl.Item(name, cost, statistic, lvl, images)


Bludgeon = create_class_item("Bludgeon", cost=40, statistic=Cl.Statistic_clothing(attack_power=(0,1), attack_p=5))
Sword_1 = create_class_item("Sword", cost=140, statistic=Cl.Statistic_clothing(attack_power=(1,2), attack_p=5), lvl=Cl.Level_system(lvl_sword=1))
Sword_2 = create_class_item("Swordi", cost=190, statistic=Cl.Statistic_clothing(attack_power=(1,2), attack_p=5), lvl=Cl.Level_system(lvl_sword=1))

s = Sword_1()

# sword
# double_hand_sword
# bow
# knife
# shield
