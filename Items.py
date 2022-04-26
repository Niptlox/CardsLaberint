TYPE_ITEM = "item"
TYPE_CLOTHING = "clothing"
TYPE_WEAPON = "weapon"

class Item():
    def __init__(self, name, cost=0, images={}, item_type=TYPE_ITEM):
        self.name = name
        self.cost = cost
        self.images = images
        self.item_type = item_type

def create_class_item(name, cost=0, images={}):
    return lambda: Item(name, cost, images)

Mouse_tale = create_class_item("mouse tale", cost=1)
Rat_tale = create_class_item("rat tale", cost=1)
