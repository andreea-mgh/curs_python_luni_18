

ITEMS = [
    {"id":1, "name":"Stick", "type":"weapon"},
    {"id":2, "name":"Helmet", "type":"helmet"},
    {"id":3, "name":"Golden Apple", "type":"consumable"},
    {"id":4, "name":"Iron Helmet", "type":"helmet"},
    {"id":5, "name":"Super Helmet", "type":"helmet"},
    {"id":6, "name":"Big Stick", "type":"weapon"},
]

class Item:
    def __init__(self, id):
        item = None
        for i in ITEMS:
            if i["id"] == id:
                item = i
        
        self.id = item["id"]
        self.name = item["name"]
        self.type = item["type"]
        self.attributes = {}

class Inventory:
    def __init__(self):
        self.items = []
        self.equipment = {
            "helmet":None,
            "armor":None,
            "boots":None,
            "weapon":None,
            "shield":None
        }
    
    def __str__(self):
        text = ""
        if len(self.items) == 0:
            return "Inventory is empty."
        else:
            text = "Inventory:\n"
            for slot, item in self.equipment.items():
                if item:
                    text += f"  {slot} slot: {item.name}\n"

            for i in self.items:
                text += f"  {i["count"]} x {i["item"].name}\n"
            return text

    def add_item(self, item):
        if type(item) == Item:
            found = False
            for i in self.items:
                if i["item"].id == item.id:
                    found = True
                    i["count"] += 1
                    break
            
            if not found:
                self.items.append({"count":1, "item":item})
    
    def remove_item(self, index):
        if index >= len(self.items):
            return
        
        if self.items[index]["count"] == 1:
            self.items.pop(index)
        else:
            self.items[index]["count"] -= 1

    def equip(self, index):
        if index >= len(self.items):
            return
        
        t = self.items[index]["item"].type
        if t in self.equipment.keys():
            self.add_item(self.equipment[t])
            self.equipment[t] = self.items[index]["item"]
            self.remove_item(index)
    
    def unequip(self, slot):
        if slot in self.equipment.keys() and self.equipment[slot]:
            self.add_item(self.equipment[slot])
            self.equipment[slot] = None


inv = Inventory()

inv.add_item(Item(1))
inv.add_item(Item(3))
inv.add_item(Item(3))
inv.add_item(Item(3))
inv.add_item(Item(3))
inv.add_item(Item(6))


print(inv)

inv.equip(0)

print(inv)

inv.equip(1)

print(inv)