class Statistic():
    def __init__(self):
        self.all_Math = False
        pass


    def set_vars(self, kwargs, def_params={}):
        for v, n in def_params.items():
            if type(n) == str and n[0] == "^":
                n = n[1:]
            st = f'it = kwargs.get(v, n); self.{v} = it; {v} = it'
            exec(st)
            print(st)

    def __le__(self, obj): # <=
        return self.boolean(obj, lambda a, b: a > b)

    def __ge__(self, obj): # >=
        return self.boolean(obj, lambda a, b: a < b)

    def __lt__(self, obj): # <
        return self.boolean(obj, lambda a, b: a >= b)

    def __gt__(self, obj): # >
        return self.boolean(obj, lambda a, b: a <= b)

    def boolean(self, obj, false_func=lambda a, b: None):
        ar1 = self.list()
        ar2 = obj.list()
        for i in range(len(ar1)):
            if false_func(ar1[i], ar2[i]):
                return False
        return True

    def list(self):
        d = list(vars(self).values())
        return d

    def __sub__(self, obj):
        return self.arithmetic(obj, func=lambda a, b: [a[i] - b[i] for i in range(len(a))] if type(a) in (list, tuple) else a - b)

    def __add__(self, obj):
        return self.arithmetic(obj, func=lambda a, b: [a[i] + b[i] for i in range(len(a))] if type(a) in (list, tuple) else a + b)

    def arithmetic(self, obj, func=lambda a, b: None):
        if self.__class__ == obj.__class__ or self.all_Math:
            d = {}
            my_d = self.__dict__
            obj_d = obj.__dict__
            for k, v in my_d.items():
                v2 = obj_d.get(k)
                d[k] = func(v, v2)
            n_obj = self.__class__()
            n_obj.set_vars(d, vars(n_obj))
            return n_obj
        raise TypeError(f"unsupported operand type(s) for -: '{self.__class__}' and '{obj.__class__}'")



class Level_system(Statistic):
    def __init__(self, **kwargs):

        params = {'lvl': 1,
                  'lvl_sword': 0,
                  'lvl_double_hand_sword': 2,
                  'lvl_bow': 0,
                  'lvl_knife': 0,

                  'lvl_shield': 0,
                  }
        self.set_vars(kwargs, params)

l1 = Level_system(lvl=5)
l2 = Level_system(lvl_bow=-3, lvl=3)
l3 = l1 - l2
l4 = l1 + l2
print(l1.list())
print(l2.list())
print(l1 < l2)
print(l1 > l2)
print(l1 <= l2)
print(l1 >= l2)

class Statistic_combat(Statistic):
    def __init__(self, **kwargs):
        self.all_Math = True
        params = {'max_hp': 0, 'hp': '^max_hp', # очки здоровья
                  'max_ap': 0, 'ap': '^max_ap', # очки действия
                  'max_mp': 0, 'mp': '^max_mp', # очки маны

                  'attack_power': (0, 1),    # сила атаки
                  'crit_attac_mult': 0, # КРИТИЧЕСКЕИЙ УМНОЖИТЕЛЬ

                  'attack_p': 0,        # цена атаки
                  'move_p': 0,          # Цена движения
                  'change_p': 0,        # цена переодевания
                  'item_use_p': 0,      # цена использования предмета

                  'attac_c': 0,         # шанс атаки
                  'crit_attac_c': 0,    # шанс krit атаки
                  'block_c': 0,         # шанс блока

                  'attac_effects': [],  # еффекты атаки
                  'my_effects': [],     # мои текущие еффекты
                  }
        self.set_vars(kwargs, params)


class Statistic_clothing(Statistic):
    def __init__(self, **kwargs):
        params = {'hp': 0, 'max_hp': 0,
                  'ap': 0, 'max_ap': 0,
                  'mp': 0, 'max_mp': 0,

                  'attack_power': (0, 0),
                  'crit_attac_mult': 1,
                  'attack_p': 0,
                  'move_p': 0,
                  'change_p': 0,
                  'item_use_p': 0,

                  'attac_c': 0,
                  'crit_attac_c': 0,
                  'block_c': 0,

                  'attac_effects': [],
                  'my_effects': []}

        self.set_vars(kwargs, params)
