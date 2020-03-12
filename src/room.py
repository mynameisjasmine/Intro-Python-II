import textwrap
# Implement a class to hold room information. This should have name and
# description attributes.
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).

# * Add the ability to add items to rooms.

#   * The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.

class Room:
    def __init__(self, room_name, description, items=[]):
        self.room_name = room_name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        


         



        
    def __str__(self):
        return f" Room Name - {self.room_name}, Room Description - {self.description}"
        



