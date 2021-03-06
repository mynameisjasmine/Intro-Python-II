from item import Item
from room import Room
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_items = []
        
    def __str__(self):
            return f" Name: {self.name}, {self.current_room}"

    def get_inventory(self):
        print('You are carrying: ')
        for added_item in self.player_items:
            print(added_item)
    
    def take_item(self):
        if len(self.current_room.items) >= 1:
            for item in self.current_room.items:
              self.player_items.append(item.item_name)


# pl = Player('Damon')
# print(pl)

