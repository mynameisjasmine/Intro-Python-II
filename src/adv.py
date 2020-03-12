from room import Room
from player import Player
from item import Item
import random

#Declare all the items



# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", 
                     [
                     Item('flail', 'it can be used to fight off enemies.'),
                     Item('sword','it will give you magical powers.'),
                     Item('hammer', 'it can break through the walls.')
                     ]
                    ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together - these are associations (ie..'has a')

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']




# Main
#

# Make a new player object that is currently in the 'outside' room.

player_one = Player('Tommy', room['outside'])


# print('Player One:', player_one)
print('Hello,', player_one.name)

#getting the room items
room_items = room['outside'].items

#creating a randomizer for the room items
item_randomizer = random.choice(room_items)

flail_item = room['outside'].items[0]
sword_item = room['outside'].items[1]
hammer_item = room['outside'].items[2]


  
 





# Create the REPL command parser in `adv.py` which allows the player to move to rooms in the four cardinal directions.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



#Player gets to choose if they want to take a weapon
print('Your current location is:', player_one.current_room, item_randomizer)
armed = input('Would you like to take this weapon? --->')
    
if armed in ['y']:
        if item_randomizer == room['outside'].items[0]:
               
               print('You have chosen to take the flail. Do remember that, ',room['outside'].items[0].item_description)

        elif item_randomizer == room['outside'].items[1]:
            # player_one.player_items = room['outside'].items[1]
            player_one.player_items.append(player_one.current_room.items[1])
            print('You have chosen to take the sword. Do remember that, ',room['outside'].items[1].item_description)

        elif item_randomizer == room['outside'].items[2]:
            
            print('You have chosen to take the hammer. Do remember that, ',room['outside'].items[2].item_description)

        else:
            print('Please enter either y or n')
            
        
if armed in ['n']:
        print('You have chosen to continue unarmed...good luck!')


while True:
    print('Your current location is:', player_one.current_room, item_randomizer)
    
    player_input = input('Which direction would you like to move in? -->')
    if player_input in ['n', 's', 'e', 'w']:
        #Move to that room
        print('move ' + player_input)
        if player_input == 'n':
            if player_one.current_room.n_to is not None and item_randomizer == flail_item:
                player_one.current_room = player_one.current_room.n_to
                room['foyer'].items.append(room['outside'].items[0].item_name)
                print('The array list items in foyer:', room['foyer'].items[0:])
                
            elif player_one.current_room.n_to is not None and item_randomizer == sword_item:
                player_one.current_room = player_one.current_room.n_to
                # room['foyer'].items.append('sword')
                room['foyer'].items.append(room['outside'].items[1].item_name)
                print('The array list:', room['foyer'].items[0:])
                
            elif player_one.current_room.n_to is not None and item_randomizer == hammer_item:
                player_one.current_room = player_one.current_room.n_to
                room['foyer'].items.append(room['outside'].items[2].item_name)
                print('The array list:', room['foyer'].items[0:])

            # elif player_one.current_room.n_to == room['overlook'] and item_randomizer == sword_item and len(room['foyer'].items) == 1:
            #         room['foyer'].items.remove(room['outside'].items[1].item_name)
            #         print('Current foyer array list:', room['foyer'].items[0:])
            #         print('current room array list:', player_one.current_room.items[0:])
                
            else:
                print('You cannot move in that direction!')
            
            # if player_one.current_room.n_to == room['overlook'] and item_randomizer == sword_item and len(room['foyer'].items) == 1:
            #         room['foyer'].items.remove(room['outside'].items[1].item_name)
            #         print('Current foyer array list:', room['foyer'].items[0:])
            #         print('current room array list:', player_one.current_room.items[0:])
                
            player_one.get_inventory()
                        
        
        if player_input == 's':
            if player_one.current_room.s_to is not None:
                player_one.current_room = player_one.current_room.s_to
            else:
                print('You cannot move in that direction!')
        if player_input == 'e':
            if player_one.current_room.e_to is not None:
                player_one.current_room = player_one.current_room.e_to
            else:
                print('You cannot move in that direction!')
        if player_input == 'w':
            if player_one.current_room.w_to is not None:
                player_one.current_room = player_one.current_room.w_to
            else:
                print('You cannot move in that direction!')
                
    elif player_input == 'q':
        print('Goodbye')
        exit()
        
    else:
        print('I did not understand the command')
        







