"""
Author:         Hannah Baum
Date:           4/25/24
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    SECTION 002
Game Title:     Mow the Lawn
GitHub Link:    https://github.com/h-baum/RPGProjectHannah/tree/main

CODE DESCRIPTION: This code runs a text-based RPG game. The goal is to mow the lawn before your parents get home.
There are 5 ways to lose the game. You can pass out from dehydration, run out of time, drive without your wallet, 
drink too much and get water poisoning, or take your parents credit card and don't have all the receipts for your purchases.
There are 3 win messages. One is when you speedrun the game and make no/almost no extra moves (Best Ending), another is when you finish the game in time
but make several unnecessary moves without using the credit card, and the last is when you take the credit card so you spend your parents money, and you show the receipts.
Your next move can be selecting an item in the room, an item in your inventory, or an exit.
Drinks go straight to your inventory when selected from the room and can be drunk (selected) at any later time in the game.
The only exception to that is the stale water, which will be drunk immediately and serves the purpose of letting you start not being a little bit thirsty. 
It's not necessary, but it also shows you how drinking water changes your thirst level.
Any non-drink in your inventory will just read a description when you select it.
If you go to the mower without gas can and air filter, mower will not start. 
If you go to the car without keys, you can not go from your car to any of the shops.
If you are walking from room to room, it takes 10 minutes and hydration goes down by 1.
Driving from room to room takes 20 minutes, and hydration goes down by 1.
Mowing from room to room takes 30 minutes, and hydration goes down by 3.
You start the game with hydration of 10. Drinking anything increases hydration by 15, except for stale water which only increases hydration by 5.
You start the game with 240 minutes. 
Interacting with items in room or inventory does not decrease time or hydration, only moving rooms does. 
Mower is a permanent item in the garage, but it unlocks start mowing exit if you have the correct items in your inventory.
It is possible to pass out or run out of time as you are finishing mowing, and if that happens, you lose. 
The log file stores the turns, user input, time, hydration, and items in inventory.
"""

#import the logging module
import logging
#sets up logging so that status and inventory can be tracked throughout program
logger = logging.getLogger(__name__)
logging.basicConfig(filename='mowthelawn.log', level=logging.DEBUG)
logger.info('Start of Log for new game')
logger.info('This is the log file for mow the lawn. It should track every user input and every print()')

#exception class that displays a message whenever the user input is not in valid exits, items in room, or items in inventory
class NotFoundError(Exception):
    def __init__(self, choice, message = "Room or Item not found. Please try again."):
    #initializes the exception's message and user input
        self.choice = choice
        self.message = message

    #returns a string containing the invalid input and the error message
    def __str__(self):
        return f"{self.choice} -> {self.message}"

#AdventureMap class that has the attribute map as a dictionary
class AdventureMap:
    def __init__(self):
    #initializes the map
        self.map = {}

    #adds the room to the map dictionary
    def add_room(self, room):
        self.map[room.name] = room

    #returns the room in the map -> dict
    def get_room(self, room_name):
        return self.map[room_name]

#ItemTracker class that has the attribute map as a dictionary
class ItemTracker:
    def __init__(self):
    #initializes the map
        self.map = {}
    
    #adds the item to the map
    def add_item(self, itemname: str):
        self.map[itemname.name] = itemname
    
    #returns the item in the map -> dict
    def get_item(self, itemname: str):
        return self.map[itemname]

#PlayerStatus class that has the attributes time and hydration
class PlayerStatus:
    def __init__(self, time = 240, hydration = 9):
        #initializes player's time left and hydration level
        self.time = time
        self.hydration = hydration
    
    #returns the time left -> int
    def get_time(self):
        return self.time
    
    #returns the hydration level -> int
    def get_hydration(self):
        return self.hydration

    #update the time based on the time changing from room to room, return the current time left -> str
    def update_time(self, incoming_time: str):
        self.time = self.get_time() - incoming_time
        return self.time
    
    #update the hydration based on the time changing from room to room, return the current hydratio level
    def update_hydration(self, incoming_hydration: int):
        self.hydration = self.get_hydration() - incoming_hydration
        return self.hydration

    # returns a string containng player's time left and hydration status, updating with each room change
    def __str__(self):
        string_overall = ''
        # list containing the different levels of thirst
        Thirst_text = ['You get water poisoning and pass out.', 'You are not thirsty.', 'You are a bit thirsty.', 'You are thirsty.', 'You are very thirsty.','You pass out from dehydration.']
        # time cannot be negative
        if self.time < 0:
            self.time = 0
        # when the hydration level is greater than 45, tell player they are out of time and got water poisoning 
        if self.get_hydration() > 44:
            string_overall += f'You have 0 minutes left.\n'
            string_overall += Thirst_text[0]
        # when the hydration level is between 1 and 44, tell player how much time they have left and their hydration status
        elif self.get_hydration() > 9:
            string_overall += f'You have {self.time} minutes left.\n'
            string_overall += Thirst_text[1]
        elif self.get_hydration() > 6:
            string_overall += f'You have {self.time} minutes left.\n'
            string_overall += Thirst_text[2]
        elif self.get_hydration() > 3:
            string_overall += f'You have {self.time} minutes left.\n'
            string_overall += Thirst_text[3]
        elif self.get_hydration() > 0:
            string_overall += f'You have {self.time} minutes left.\n'
            string_overall += Thirst_text[4]
        # when hydration level is 0, tell player they are out of time and they passed out from dehydration
        else:
            string_overall += f'You have 0 minutes left.\n'
            string_overall += Thirst_text[5]
        return string_overall

#SuperItem class with the attributes name, itemtype, pickuptext, and inventorytext
#This class is the superclass for the subclasses Purchase, Pickup, Permanent, and Wallet
class SuperItem:
    def __init__(self, name, itemtype, pickuptext, inventorytext):
    #initializes item's name, type, text when picked up, and text when selected while in inventory
        self.name = name
        self.item_type = itemtype
        self.pickup_text = pickuptext
        self.inventory_text = inventorytext

    #returns item's name -> str
    def get_name(self):
        return self.name

    #returns item type -> str
    def get_item_type(self):
        return self.item_type

    #returns item's text when picked up -> str
    def get_pickup_text(self):
        return self.pickup_text

    #returns item's text when selected while in inventory -> str
    def get_inventory_text(self):
        return self.inventory_text

#Purchase subclass of SuperItem 
#affects items that are purchasable, such as Boba Tea, Coffee, Air Filter, and Gas Can
class Purchase(SuperItem):
    #initializes purchasable item's name, type, text when picked up, and text when selected while in inventory
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    #
    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

#
class Pickup(SuperItem):
    #
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)
    
    #
    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

#
class Permanent(SuperItem):
    #
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    #
    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

#
class Wallet(SuperItem):
    #
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    #
    def displayinfo(self, text_id, money_left):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
            string_overall += str(money_left)
            string_overall += ' in it.'
        return string_overall

#Room class contains descriptors of the room
class Room:
    #initializes the room name, room description, list of exits, list of unlockable exits, list of items in room, time remaining, hydration level
    def __init__(self, name, description, exits, unlockable_exit, items, time, hydration):
        self.name = name
        self.description = description
        self.exits = exits
        self.unlockable_exit = unlockable_exit
        self.items = items
        self.time = time
        self.hydration = hydration

    #returns name of the room -> str
    def get_name(self):
        return self.name
    
    #returns description of the room -> str
    def get_description(self):
        return self.description
    
    #returns list of exits -> list
    def get_exits(self):
        return self.exits

    #returns a string of exits from the list of exits, deletes last comma
    def list_exits(self):
        string_exits = ""
        for i in self.get_exits():
            string_exits += f"{i}, "
        string_exits = string_exits[:-2]
        return string_exits

    #returns list of unlockable exits -> list
    def get_unlockable_exit(self):
        return self.unlockable_exit

    #adds the list of newly unlocked exits to the overall list of exits for that room, returns a list of exits
    def update_exits(self):
        for i in range(len(self.unlockable_exit)):
            self.get_exits().append(self.unlockable_exit[i])
        #the newly unlocked exits can not be added again by meeting the same criteria, they are permanently unlocked
        self.get_unlockable_exit().clear()
        return self.exits

    #returns a list of items in the room -> list
    def get_items(self):
        return self.items
    
    #returns the time -> int
    def get_time(self):
        return self.time

    #returns the hydration -> int
    def get_hydration(self):
        return self.hydration

    #returns a string of items from the list of items, deletes last comma
    def list_items(self):
        string_items = ""
        for i in self.get_items():
            string_items += f"{i}, "
        string_items = string_items[:-2]
        return string_items

    #adds the items to the room, returns list of current items in room
    def add_items(self, item_to_add):
        self.get_items().append(item_to_add)
        return self.items

    #removes items from the room, returns list of current items in room
    def update_items(self, item_to_remove):
        self.get_items().remove(item_to_remove)
        return self.items

    #returns string containing the room name, description, list of exits, and list of items in the room
    def __str__(self):
        string_overall = ""
        string_overall += f"{self.get_name()}: "
        string_overall += f"{self.get_description()}\n\n"
        string_overall += f"Exits: {self.list_exits()}\n"
        string_overall += f"Items in room: {self.list_items()}"
        return string_overall

def main():
    #initialize number of turns
    turn = 1
    #oprn log file in writing mode
    X = open('MowTheLawn.txt', 'w')

    #calls map and status classes
    adventure_map = AdventureMap()
    current_status = PlayerStatus()
    #room: name, description, [exits], [unlockable exits], [items], time, hydration
    #add the rooms to the map
    #House rooms
    adventure_map.add_room(Room("Bedroom", "A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?", ['Kitchen', 'Master Bedroom'], [], ["Note", "Wallet", "Stale Water"], 10, 1))
    adventure_map.add_room(Room("Kitchen", "A room with a leaky sink and an near-empty fridge, containing only several water bottles.", ['Garage', 'Master Bedroom', 'Bedroom'], [], ["Grab Water", "Keys"], 10, 1))
    adventure_map.add_room(Room("Master Bedroom", "Your parents keep their room clean and tidy. The beds are nicely made, the clothes are folded and put away. Maybe you could take some hints?", ['Kitchen', 'Bedroom'], [], ["Credit Card"], 10, 1))
    adventure_map.add_room(Room("Garage", "There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.", ['Kitchen', 'Front Yard', 'Back Yard', 'Car'], ['Start Mowing'], ["Mower"], 10, 1))
    adventure_map.add_room(Room("Start Mowing", "You successfully start the mower.", ['Mow Front', 'Mow Back', 'Garage'], [], [], 10, 1))
    adventure_map.add_room(Room("Car", "You get inside the vehicle. If you have keys, you can drive to many places.", ['Garage'], ['Boba Shop','Coffee Shop','Gas Station','Hardware Store'], [], 10, 1))
    #Outside locations
    adventure_map.add_room(Room("Boba Shop", "You drive to a shop stocked with all the delicious boba drinks you could imagine!!!", ['Garage', 'Coffee Shop', 'Gas Station','Hardware Store'], [], ['Boba Tea'], 20, 2))
    adventure_map.add_room(Room("Coffee Shop", "You drive to a shop stocked with many caffeinated drinks.", ['Garage', 'Boba Shop', 'Gas Station','Hardware Store'], [], ['Coffee'], 20, 2))
    adventure_map.add_room(Room("Gas Station", "You drive to a store containing gas for your lawn mower.", ['Garage', 'Boba Shop', 'Coffee Shop','Hardware Store'], [], ['Gas Can'], 20, 2))
    adventure_map.add_room(Room("Hardware Store", "You drive to a store containing air filters for your lawn mower.", ['Garage','Gas Station','Boba Shop','Coffee Shop'], [], ['Air Filter'], 20, 2))
    #Yard pieces
    adventure_map.add_room(Room("Back Yard", "You walk to the back yard. You aren't looking forward to mowing it.", ['Garage', 'Front Yard'], [], [], 10, 1))
    adventure_map.add_room(Room("Front Yard", "You walk to the front yard. You aren't looking forward to mowing it.", ['Back Yard','Garage'], [], [], 10, 1))
    adventure_map.add_room(Room("Mow Back", "You mow the back yard.", ['Mow Front', 'Garage'], [], [], 30, 5))
    adventure_map.add_room(Room("Mow Front", "You mow the front yard.", ['Mow Back', 'Garage'], [], [], 30, 5))

    # intiailize amount of money left and number of purchases
    money_left = 0
    purchase_count = 0

    #calls item tracker classes
    item_tracker = ItemTracker()

    #item: name, type of item, pickup text, interact text
    #non-drinkable, purchasable item, enters inventory
    item_tracker.add_item(Purchase('Gas Can','Purchase Item','You attempt to purchase a can of gas for $5.','It is a can of gas.'))
    item_tracker.add_item(Purchase('Air Filter', 'Purchase Item', 'You attempt to purchase an air filter for $5.','It is an air filter.'))
    #drinkable, purchasable item, enters inventory
    item_tracker.add_item(Purchase('Boba Tea', 'Purchase Drink', 'You attempt to purchase a boba tea for $5.', 'You drink the boba tea, and feel refreshed.'))
    item_tracker.add_item(Purchase('Coffee', 'Purchase Drink', 'You attempt to purchase a coffee for $5.', 'You drink the coffee, and feel energized.'))
    #enters inventory
    item_tracker.add_item(Pickup('Keys', 'Pickup', 'You have picked up a key chain.', 'It is a key chain.'))
    item_tracker.add_item(Pickup('Credit Card', 'Pickup', 'You take your parents credit card.', 'You wonder if your parents will notice you took it. Oh well, you are going to use it for all your purchases. Surely it will be fine.'))
    item_tracker.add_item(Pickup('Gas Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the gas station.'))
    item_tracker.add_item(Pickup('Filter Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the hardware store.'))
    item_tracker.add_item(Pickup('Boba Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the boba shop.'))
    item_tracker.add_item(Pickup('Coffee Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the coffee shop.'))
    item_tracker.add_item(Wallet('Wallet', 'Pickup', 'You pick up your wallet. It has $10 in it as well as your license.', 'It is a wallet with your license and $'))
    item_tracker.add_item(Pickup('Note', 'Pickup', 'It is a note that says, "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We will be back at 4pm, so get moving!"', 'The note says, "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We will be back at 4pm, so get moving!"'))
    item_tracker.add_item(Pickup('Water Bottle', 'Pickup Drink', '', 'You drink the water. Gotta stay hydrated.'))    
    #permanently in the room, even after being interacted with, it stays in the room for future interactions, never enters inventory
    item_tracker.add_item(Permanent('Mower', 'Permanent', 'You try to start the mower, but nothing happens. Maybe it needs something.','You fill the mower with gas and replace the air filter, and it starts! Congratulations, better start mowing.'))
    item_tracker.add_item(Permanent('Grab Water', 'Permanent', 'You take a water bottle from the fridge.', "You already have one, so what are you doing? Don't be greedy."))
    #never enters inventory, immediately gone from room upon interaction
    item_tracker.add_item(Pickup('Stale Water', 'Instant Drink', 'You drink the stale water. Better than nothing.', ''))

    #prints and logs opening lines
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Mow the Lawn! Do your best to mow the lawn today.\n")
    logger.info("Welcome to Mow the Lawn! Do your best to mow the lawn today.\n")
    X.write("Welcome to Mow the Lawn! Do your best to mow the lawn today.\n")
    X.write(f'Turn {turn}\n')
    print("You wake up in your room. Next to you there is a note on the table next to the bed, as well as a cup of room-temperature water. It's currently noon, and you're feeling a bit thirsty.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #initializes inventory as a list
    current_inventory = []
    #intializes room, you wake up in your bedroom
    current_room = 'Bedroom'
    #tells user room description
    print(adventure_map.get_room(current_room))
    #initializes inventory as a string
    string_inventory = ""
    #adds list of items from inventory to string, gets rid of final comma
    for i in current_inventory:
        string_inventory += f"{i}, "
    string_inventory = string_inventory[:-2]
    #tells user and logs their items in inventory
    print(f'Items in inventory: {string_inventory}\n')
    logger.info(f'Items in inventory: {string_inventory}\n')
    X.write(f'Items in inventory: {str(string_inventory)}\n')
    #tells user and logs their current status based on time left and hydration level
    print(current_status)
    logger.info(current_status)
    logger.info(f'Hydration level:{current_status.get_hydration()}')
    X.write(f'Time remaining: {current_status.get_time()}\n')
    X.write(f'Hydration level:{str(current_status.get_hydration())}\n')

    #initially, player has not mowed the front or back yard
    mowed_front = 0
    mowed_back = 0
    Continue = True
    #game continues as long as player has not won or lost, can not lose based on player input
    while Continue == True:
        #when player's hydration goes to 0 or above 45, the game is over (LOSS 1,2)
        if current_status.get_hydration() <= 0 or current_status.get_hydration() >= 44: 
            print('Game over.')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            logger.info('Game over.')
            X.write('Game over.\n\n')
            exit()
        #when player's time runs out, the game is over (LOSS 3)
        elif current_status.get_time() <= 0:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("You ran out of time. Your parents are pulling into the driveway. Expect to be grounded for the next two weeks.")
            print('Game Over.')
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            logger.info("You ran out of time. Your parents are pulling into the driveway. Expect to be grounded for the next two weeks.")
            X.write("You ran out of time. Your parents are pulling into the driveway. Expect to be grounded for the next two weeks.\n")
            logger.info('Game Over.')
            X.write('Game Over.\n\n')
            exit()
        #when the player has mowed both the front and back yard (completed the game), end the program
        elif (mowed_back + mowed_front == 2):
            #when player has credit card and does not have receipts for all their purchases, they lose (LOSS 4)
            if 'Credit Card' in current_inventory and purchase_count != 0:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Congrats, you have mowed the lawn. However, you were immediately grounded when they found you took their credit card and were not able to prove what you spend it on.')
                print('You lost, do better next time and maybe your parents will be proud of you.')
                print('Game Over.')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                logger.info('Congrats, you have mowed the lawn. However, you were immediately grounded when they found you took their credit card and were not able to prove what you spend it on.')
                logger.info('You lost, do better next time and maybe your parents will be proud of you.')
                logger.info('Game Over.')
                X.write('Congrats, you have mowed the lawn. However, you were immediately grounded when they found you took their credit card and were not able to prove what you spend it on.\n')
                X.write('You lost, do better next time and maybe your parents will be proud of you.\n')
                X.write('Game Over.\n\n')
            #when player has credit card and has receipts for all their purchases at the end of game, they win (WIN 1)
            elif 'Credit Card' in current_inventory and purchase_count == 0:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.')
                print('You win, but maybe things could have gone a little better.')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                logger.info('Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.')
                logger.info('You win, but maybe things could have gone a little better.')
                X.write('Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.\n')
                X.write('You win, but maybe things could have gone a little better.\n\n')
            #when player still has at least 60 minutes left at the end of the game, they win (WIN 2)(BEST ENDING)
            elif current_status.get_time() >= 60:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.')
                print('You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.')
                print('Good job! Keep it up.')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                logger.info('Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.')
                logger.info('You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.')
                logger.info('Good job! Keep it up.')
                X.write('Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.\n')
                X.write('You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.\n')
                X.write('Good job! Keep it up.\n\n')
            #when player has reached the end of game and not met either of other endings, final win message (WIN 3)
            else:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('Congrats, you have mowed the lawn! Your parents are very happy.')
                print('You Won!')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                logger.info('Congrats, you have mowed the lawn! Your parents are very happy.')
                logger.info('You Won!')
                X.write('Congrats, you have mowed the lawn! Your parents are very happy.\n')
                X.write('You Won!\n\n')
            exit()

        #ask the user to input what they want to do next, fix capitalization and remove trailing whitespace
        print('\nWhat would you like to do?')
        tempchoice = input()
        Choice = tempchoice.title().strip()
        logger.info(f'User input: {tempchoice} -> {Choice}.')
        X.write(f'User input: {tempchoice} -> {Choice}.\n\n')
        turn +=1 
        X.write(f'Turn {turn}\n')

        try:
            #raise custom exception class when user inputs an option that is not a valid exit or valid item in room/inventory
            if (Choice not in adventure_map.get_room(current_room).get_exits()) and (Choice not in adventure_map.get_room(current_room).get_items()) and (Choice not in current_inventory):
                raise NotFoundError(Choice)
            #when user chooses an exit, update current room, loop
            if Choice in adventure_map.get_room(current_room).get_exits():
                #if the player drives home without their wallet, the game ends (LOSS 5)
                if current_room == 'Gas Station' or current_room == 'Hardware Store' or current_room == 'Boba Shop' or current_room == 'Coffee Shop':
                    if Choice == 'Garage' and 'Wallet' not in current_inventory:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print('You got pulled over at a traffic stop on the way home and were found to be driving without a license.')
                        print('You did not pass go and did not collect 200 dollars, and were sent directly to jail.')
                        print('Game Over.')
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        X.write('You got pulled over at a traffic stop on the way home and were found to be driving without a license.\n')
                        X.write('You did not pass go and did not collect 200 dollars, and were sent directly to jail.\n')
                        X.write('Game Over.\n\n')
                        break
                #if the player mows the front yard, half of criteria for winning met
                if Choice == 'Mow Front':
                    mowed_front = 1
                #if the player mows the front yard, half of criteria for winning met
                elif Choice == 'Mow Back':
                    mowed_back = 1
                #set current room as choice
                current_room = Choice
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #tell player the description of the room
                print(adventure_map.get_room(current_room))
                #initialize inventory as string
                string_inventory = ""
                #add items from inventory list to inventory string, delete final comma 
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                #print out and log the items in player's inventory
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                X.write(f'Items in inventory: {string_inventory}\n')
                #update player's status, based on changes in time remaining and hydration levels
                current_status.update_time(adventure_map.get_room(current_room).get_time())
                current_status.update_hydration(adventure_map.get_room(current_room).get_hydration())
                #tell user and log their status
                print(current_status)
                logger.info(current_status)
                logger.info(f'Hydration level: {current_status.get_hydration()}')
                X.write(f'Time remaining: {current_status.get_time()}\n')
                X.write(f'Hydration level: {current_status.get_hydration()}\n')
                
            #user chooses an item in the room
            #print item pickup line, loop
            # may call room.update item, also room.update exits
            elif Choice in adventure_map.get_room(current_room).get_items():
                #signifies whether user can afford item
                item_success = True
                #when user picks up wallet, there are 10 dollars in it initially
                if Choice == 'Wallet':
                    money_left += 10
                #when user buys something from a shop, they lose 5 dollars as long as they can afford it
                elif Choice == 'Boba Tea' or Choice == 'Coffee' or Choice == 'Gas Can' or Choice == 'Air Filter':
                    #if they have at least 5 dollars, they successfully buy the item
                    if money_left >= 5:
                        money_left -= 5
                        item_success = True
                    #when user has a credit card, you can buy everything because there's 2000 dollars on it 
                    elif 'Credit Card' in current_inventory:
                        item_success = True
                    #when user can't afford it, they do not succesully purchase the item
                    else:
                        item_success = False
                    #when they successfully purchase an item, update number of purchases 
                    if item_success == True:
                        purchase_count += 1
                        #add the item's receipt to the room where they just bought an item, they can pick this up
                        if Choice == 'Boba Tea':
                            adventure_map.get_room(current_room).add_items("Boba Receipt")
                        elif Choice == 'Coffee':
                            adventure_map.get_room(current_room).add_items("Coffee Receipt")
                        elif Choice == 'Gas Can':
                            adventure_map.get_room(current_room).add_items("Gas Receipt")
                        elif Choice == 'Air Filter':
                            adventure_map.get_room(current_room).add_items("Filter Receipt")
                #if user picks up keys, the shops are now able to be driven from the car
                #before this, if the user was in the car, they could only exit to the garage
                elif Choice == 'Keys':
                    adventure_map.get_room('Car').update_exits()
                    logger.info('New exits have been added to the car.')
                    X.write('New exits have been added to the car.\n')
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #if the user does not have enough money for the item, tell them they don't have enough and to find more
                if item_success == False:
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    print("You cannot afford this item. Go search the house for some change?")
                    X.write('Insufficient money\n')
                #when the user chooses the mower, it can either unlock start mowing or just prints message saying they are missing something
                elif Choice == 'Mower':
                    if 'Gas Can' in current_inventory and 'Air Filter' in current_inventory:
                        print(item_tracker.get_item(Choice).displayinfo(2))
                        adventure_map.get_room('Garage').update_exits()
                        logger.info('New exit has been added to the garage.')
                        X.write('New exit has been added to the garage.\n')
                        #clicking on the mower starts it if you have the required items
                    else:
                        print(item_tracker.get_item(Choice).displayinfo(1))
                        #you cannot put the mower in your inventory
                elif Choice == 'Stale Water':
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    current_status.update_hydration(-5)
                    adventure_map.get_room(current_room).update_items(Choice)
                    #stale water cannot be put in inventory so it gets immediately drunk
                    #but it does disappear from the room
                elif Choice == 'Grab Water':
                    if 'Water Bottle' not in current_inventory:
                        print(item_tracker.get_item(Choice).displayinfo(1))
                        current_inventory.append('Water Bottle')
                        #you cannot put multiple water bottles in your inventory, only 1 water bottle
                        #water bottles does not disappear from the room, you can drink the water bottle and pick up another one
                    else:
                        print(item_tracker.get_item(Choice).displayinfo(2))
                elif Choice == 'Wallet':
                    print(item_tracker.get_item(Choice).displayinfo(1, money_left))
                    adventure_map.get_room(current_room).update_items(Choice)
                    current_inventory.append(Choice)
                    #tell the user how much money in their wallet and take it from the room to the inventory
                else:
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    adventure_map.get_room(current_room).update_items(Choice)
                    current_inventory.append(Choice)
                    #every other item goes in your inventory
                #when user picks up receipts, the counted number of purchases goes down (matters only if credit card was picked up)
                if item_tracker.get_item(Choice).get_item_type() == 'Pickup Receipt':
                    purchase_count -= 1
                #since user picks up an item from a room, tell them the room description (which didn't change) and their updated inventory
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(adventure_map.get_room(current_room))
                string_inventory = ""
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                X.write(f'Items in inventory: {string_inventory}\n')
                #tell the user and log their current status, based on hydration and time remaining
                print(current_status)
                logger.info(current_status)
                logger.info(f'{current_status.get_hydration()} is your water level.')
                X.write(f'Time remaining: {current_status.get_time()}\n')
                X.write(f'Hydration level: {str(current_status.get_hydration())}.\n')

            #when player chooses an item in their inventory
            #print item interact line, loop
            elif Choice in current_inventory:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #if they select the wallet, it will print out a message saying how much money is left in it, updates with each purchase if you don't have the credit card
                if Choice == 'Wallet':
                    print(item_tracker.get_item(Choice).displayinfo(2, money_left))
                #if they drink something in their inventory, a message is printed out saying what they drank, and their hydration level updates
                #the choice is "used up" (disappears from their inventory)
                elif item_tracker.get_item(Choice).get_item_type() == 'Purchase Drink' or item_tracker.get_item(Choice).get_item_type() == 'Pickup Drink':
                    print(item_tracker.get_item(Choice).displayinfo(2))
                    current_inventory.remove(Choice)
                    current_status.update_hydration(-15)
                else:
                #if they select a nondrinkable item, it just prints out the informational message
                    print(item_tracker.get_item(Choice).displayinfo(2))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #print out description of the room
                print(adventure_map.get_room(current_room))
                string_inventory = ""
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                #print out and log the items in current inventory
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                X.write(f'Items in inventory: {string_inventory}\n')
                #print out and log player's updated status, based on time remaining and hydration level
                print(current_status)
                logger.info(current_status)
                logger.info(f'{current_status.get_hydration()} is your water level.')
                X.write(f'Time remaining: {current_status.get_time()}\n')
                X.write(f'Hydration level: {str(current_status.get_hydration())}\n')

        #when user inputs something that is not a valid exit, item in room, or item in inventory
        #print out and log error message, they will be asked to input a valid choice
        except NotFoundError:
            print(NotFoundError(Choice))
            logger.warning(NotFoundError(Choice))
            X.write(f'Warning: {str(NotFoundError(Choice))}\n')
    #close the log file
    X.close()

#runs main
if __name__ == "__main__":
    main()