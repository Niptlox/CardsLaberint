class Room():
    def __init__(self, xy=(0, 0), num=None, name="",
                 lock=False, mobs=[], chest=None):
        self.num = num
        self.name = name
        self.lock = lock
        self.x, self.y = xy
        self.mobs = mobs
        self.chest = chest

    def go_in_room(self):
        return not self.lock

    def get_xy(self):
        return (self.x, self.y)

    def add_mobs(self, mobs):
        for mob in mobs:
            self.add_mob(mob)

    def add_mob(self, mob):
        self.mobs.append(mob)


class Field_lab():

    def __init__(self, name, entry_xy=(0, 0)):
        self.field = {}
        self.name = name
        self.entry_xy = entry_xy

    def set_obj(self, obj, room):
        room.add_mob(obj)

    def add_room(self, room, passages=[]):
        self.field[room.get_xy()] = [room, passages]

    def get_room(self, xy):
        return self.field.get(xy)

    def set_entry_xy(self, xy):
        self.entry_xy = xy

    def get_entry_xy(self):
        return self.entry_xy

    def get_entry_room(self):
        return self.field.get(self.entry_xy)
