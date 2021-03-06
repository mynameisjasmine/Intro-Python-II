from room import Room
from player import Player
from item import Item
import random

#Declare all the items.



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
passages run north and east.""", [Item('flashlight', 'this flashlight can help you see in dark rooms')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('crystal ball', 'a glowing crystal that lights up')]),

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

# items_inventory = player_one.current_room.items[0:]


  
 





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
               
               print('You have chosen to take the flail. Do remember that,',flail_item.item_description)

        elif item_randomizer == room['outside'].items[1]:
    
            print('You have chosen to take the sword. Do remember that,',sword_item.item_description)
        

        elif item_randomizer == room['outside'].items[2]:
            
            print('You have chosen to take the hammer. Do remember that,',hammer_item.item_description)

        else:
            print('Please enter either y or n')
            
        
if armed in ['n']:
        print('You have chosen to continue unarmed...good luck!')

if armed == 'q':
        print('Goodbye')
        exit()

while True:
    # print('Your current location is:', player_one.current_room, item_randomizer)
    print('Your current location is:', player_one.current_room.room_name)

    
    player_input = input('Which direction would you like to move in? -->')
    if player_input in ['n', 's', 'e', 'w']:
        #Move to that room
        print('Move ' + player_input)
        if player_input == 'n':
            if player_one.current_room.n_to is not None and item_randomizer == flail_item:
                if 'flail' not in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    # Append the chosen weapon to the player items array
                    player_one.player_items.append(flail_item.item_name)
                    
                    # Get a list of any weapons hidden in the current room
                    player_one.current_room.get_room_items()

                elif 'flail' in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    player_one.current_room.get_room_items()


                


                
            elif player_one.current_room.n_to is not None and item_randomizer == sword_item:
                if 'sword' not in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    # Append the chosen weapon to the player items array
                    player_one.player_items.append(sword_item.item_name)
                    
                    # Get a list of any weapons hidden in the current room
                    player_one.current_room.get_room_items()

                elif 'sword' in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    player_one.current_room.get_room_items()




                
            elif player_one.current_room.n_to is not None and item_randomizer == hammer_item:
                if 'hammer' not in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    # Append the chosen weapon to the player items array
                    player_one.player_items.append(hammer_item.item_name)
                    
                    # Get a list of any weapons hidden in the current room
                    player_one.current_room.get_room_items()
                
                elif 'hammer' in player_one.player_items:
                    player_one.current_room = player_one.current_room.n_to
                    player_one.current_room.get_room_items()




            # elif player_one.current_room.n_to == room['overlook'] and item_randomizer == sword_item and len(room['foyer'].items) == 1:
            #         room['foyer'].items.remove(room['outside'].items[1].item_name)
            #         print('Current foyer array list:', room['foyer'].items[0:])
            #         print('current room array list:', player_one.current_room.items[0:])
                
            else:
                print('You cannot move in that direction!')
            
          
                
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

            
            player_one.get_inventory()
    if player_input == 'q':
        print('Goodbye')
        exit()
    # else:
    #     print('I did not understand the command')
        
    # If the room contains an item player get option to pick up the item
    pick_up_item = input('Would you like to pick up the item in this room? ------>')
           
    if player_one.current_room.items is not None:
        # pick_up_item = input('Would you like to pick up the item in this room? ------>')
        if pick_up_item in ['y', 'n']:
            if pick_up_item == 'y':
                player_one.take_item()
                player_one.get_inventory()
                # print('Your current location is:', player_one.current_room.room_name)
            
            elif pick_up_item == 'n':
                player_one.get_inventory()
                 
    elif player_one.current_room.items is None:
          player_one.get_inventory()
    
    
    if pick_up_item == 'q':
        print('Goodbye')
        exit()

    # if player_input == 'q':
    #     print('Goodbye')
    #     exit()
        
    # else:
    #     print('I did not understand the command')
        







