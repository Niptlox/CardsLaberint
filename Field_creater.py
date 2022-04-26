import Field
import Entitys
import pickle

def map_creater(name, list_map, dictory, entry_xy=(0, 0)):
    field = Field.Field_lab(name)
    n, m = len(list_map), len(list_map[0])
    print(n, m)
    for y in range(n):
        for x in range(m):
            room = list_map[y][x]
            if room:
                mobs = []
                if type(room) == list:
                    mob, c = room
                    mob = dictory[mob]
                    mobs = [mob() for i in range(c)]
                room = Field.Room(xy=(x, y), mobs=mobs)
                field.add_room(room)
    name_file = f"maps/{name}.lmap"
    map_file = open(name_file, "wb")
    date = field
    pickle.dump(date, map_file)
    map_file.close()

def load_map(name):
    name_file = f"maps/{name}.lmap"
    map_file = open(name_file, "rb")
    data = pickle.load(map_file)
    return data


if __name__ == "__main__":
    m = "mouse"
    r = "rat"
    d = {
         m: Entitys.Mouse,
         r: Entitys.Rat,
    }
    room__ = "room"
    None__ = None
    Name = "Laberint Oratori"
    if Name:
        ar = [
    [room__, [m, 1], room__,],
    [[m, 2], None__, [m, 4],],
    [[r, 1], [r, 1], [r, 3],],
        ]
        map_creater(Name, ar, d, entry_xy=(0, 0))
