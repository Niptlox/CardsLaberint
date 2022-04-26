import random
import Items as It
from Statistic import Statistic_combat, Level_system


s = Statistic_combat(hp=10)
print(vars(s))

def rchance(chance):
    return chance >= random.randint(1, 100)

class Entity():
    def __init__(self, name, statistic_combat=Statistic_combat(), inventory=[],
                 dressed_items=[], xp=0,
                 money=0, enemy=False, xy=(0, 0), room=None,
                 items_die=[]): # **kwargs):
        self.name = name
        self.my_statistic_combat = statistic_combat
        self.statistic_combat = statistic_combat
        self.inventory = inventory
        self.dressed = {"arms": [None, None], "glove": None,
                        "boots": None, "body": None,
                        "trausers": None, "rings": [None, None],
                        "hat": None, "neclace": None } # одетые предметы (neclace ожерелье)
        self.dress_items(dressed_items)
        self.xp = xp
        self.money = money
        self.enemy = enemy
        self.x, self.y = xy
        self.status = []
        self.room = room
        self.update_statistic_combat()
        if items_die:
            self.items_die = items_die
        else:
            self.items_die = self.inventory

    def update_statistic_combat(self, items=None):
        if items is None:
            self.statistic_combat = self.my_statistic_combat
            items = self.dressed.values()
        for item in items:
            if item is None:
                pass
            elif type(item) == list:
                self.update_statistic_combat(item)
            else:
                self.statistic_combat = self.statistic_combat + item.statistic

    def dress_items(self, items):
        for item in items:
            self.auto_dress_item(item)

    def auto_dress_item(self, item):
        if item.item_type == It.TYPE_WEAPON:
            self.dress_weapon(item)

    def dress_weapon(self, item, arm=0):
        if self.dressed["arms"][arm] == None:
            self.dressed["arms"][arm] = item


    def get_room(self):
        return self.room

    def set_room(self, room):
        self.room = room

    def set_xy(self, xy):
        self.y, self.x = (xy)

    def get_xy(self):
        return (self.x, self.y)

    def add_xy(self, x=0, y=0):
        self.x += x
        self.y += y

    def remove_status(self):
        status = self.status
        self.status = []
        return status

    def add_status(self, status):
        self.status.append(status)

    def get_last_status(self, status):
        return bool(status) and self.status[-1]

    def remove_last_status(self, status):
        return bool(status) and self.status.pop(-1)

    def update(self, tick=0):
        pass

    def update_my_effects(self):
        i = 0
        while i < len(self.statistic_combat.my_effects):
            if effect.update(self):
                i += 1

    def add_me_effect(self, effect):
        self.statistic_combat.my_effects.append(effect)

    def get_my_attac_effects(self):
        effects = self.statistic_combat.attac_effects
        return effects

    def get_my_items_attac_effects(self):
        effects = []
        for item in self.dressed_items:
            effects += item.get_attac_effects
        return effects

    def get_my_damage(self):
        d = 0
        dc = self.statistic_combat.attac_c
        r = random.randint(1, 100)
        if dc >= r:
            d = self.statistic_combat.attack_power
            self.add_status("attac")
        cc = self.statistic_combat.crit_attac_c
        r = random.randint(1, 100)
        if cc >= r:
            self.add_status("crit_attac")
            d *= self.statistic_combat.crit_attac_mult
        return d

    def get_my_damage(self):
        d = 0
        dc = self.statistic_combat.attac_c
        r = random.randint(1, 100)
        if dc >= r:
            d = self.statistic_combat.attack_power
            self.add_status("attac")
        cc = self.statistic_combat.crit_attac_c
        r = random.randint(1, 100)
        if cc >= r:
            self.add_status("crit_attac")
            d *= self.statistic_combat.crit_attac_mult
        return d

    def punch_me(self, punch):
        damage = punch["damage"]
        if rchance(self.chance_protect):
            self.add_status("protect")
            return False
        self.lifes -= damage
        effects = punch["effects"]
        for effect in effects:
            self.add_me_effect(effect)
        return True

    def get_punch(self, type="my"):
        if type == "my":
            punch["damage"] = self.get_my_damage()
            punch["effects"] = self.get_my_attac_effects() + self.get_my_items_attac_effects()
        # punch[]
        return punch

    def get_items_die(self):
        items = []
        for item in self.items_die:
            ic = 100
            try:
                item, ic = item
            except:
                item = item
            if rchance(ic):
                items.append(item)
        money = self.money
        xp = self.xp
        return {"xp": xp, "money": money, "items": items}

    def update_die(self, get_items=True):
        hp = self.statistic_combat.hp
        if hp < 1:
        	items = self.get_items_die()
        	if items:
        		return items
        	return True
        return False



class Mouse(Entity):
    def __init__(self):
        statistic_combat = Statistic_combat(max_hp = 3, max_ap=1, attack_power=1, attack_p=1, attac_c=20, block_c=1)
        super().__init__("mouse", statistic_combat, money=2, xp=1, enemy=True, items_die=[Mouse_tale()])


class Rat(Entity):
    def __init__(self):
        statistic_combat = Statistic_combat(max_hp=5, max_ap=1, attack_power=2, attack_p=1, attac_c=30, block_c=5)
        super().__init__("rat", statistic_combat, money=3, xp=2, enemy=True, items_die=[Rat_tale()])
