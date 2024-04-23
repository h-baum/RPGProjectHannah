"""
Author:         Hannah Baum
Date:           4/20/24
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    SECTION 002

CODE DESCRIPTION: This code runs a text-based RPG game. The goal is to mow the lawn before your parents get home.
There are 5 ways to lose the game. You can pass out from dehydration, run out of time, drive without a license then go to jail, 
drink too much and get water poisoning, or take your parents credit card and don't have all the receipts for your purchases.
There are 3 win messages. One is when you speedrun the game and make no/almost no extra moves (Best Ending), another is when you finish the game in time
but make several unnecessary moves without using the credit card, and the last is when you take the credit card so you spend your parents money, and you show the receipts.


"""
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='mowthelawn.log', level=logging.DEBUG)
#logging.basicConfig(format='%(asctime)s %(message)s')
logger.info('\nThis is the log file for mow the lawn. It should track every user input and every print')

#logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.basicConfig(
#     format='%(asctime)s %(levelname)-8s %(message)s',
#     level=logging.INFO,
#     datefmt='%Y-%m-%d %H:%M:%S')
# logging.warning('is when this event was logged.')

class NotFoundError(Exception):
    def __init__(self, room_name, message = "Room or Item not found. Please try again."):
        self.room_name = room_name
        self.message = message

    def __str__(self):
        return f"{self.room_name} -> {self.message}"

class AdventureMap:
    def __init__(self):
        self.map = {}

    def add_room(self, room):
        self.map[room.name] = room

    def get_room(self, room_name):
        return self.map[room_name]

class ItemTracker:
    def __init__(self):
        self.map = {}
    
    def add_item(self, itemname):
        self.map[itemname.name] = itemname
    
    def get_item(self, itemname):
        return self.map[itemname]

class PlayerStatus:
    def __init__(self, time = 250, hydration = 10):
        self.time = time
        self.hydration = hydration
    
    def get_time(self):
        return self.time
    
    def get_hydration(self):
        return self.hydration

    def update_time(self, incoming_time):
        self.time = self.get_time() - incoming_time
        return self.time
    
    def update_hydration(self, incoming_hydration):
        self.hydration = self.get_hydration() - incoming_hydration
        return self.hydration

    def __str__(self):
        string_overall = ''
        #string_overall += f'You have {self.time} minutes left.\n'
        Thirst_text = ['You get water poisoning and pass out.', 'You are not thirsty.', 'You are a bit thirsty.', 'You are thirsty.', 'You are very thirsty.','You pass out from dehydration.']
        if self.time < 0:
            self.time = 0
        if self.get_hydration() > 44:
            string_overall += f'You have 0 minutes left.\n'
            string_overall += Thirst_text[0]
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
        else:
            string_overall += f'You have 0 minutes left.\n'
            string_overall += Thirst_text[5]
        return string_overall

class SuperItem:
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        self.name = name
        self.item_type = itemtype
        self.pickup_text = pickuptext
        self.inventory_text = inventorytext

    def get_name(self):
        return self.name

    def get_item_type(self):
        return self.item_type

    def get_pickup_text(self):
        return self.pickup_text
        
    def get_inventory_text(self):
        return self.inventory_text
    #def __str__(self, pickup_id):
    #    string_overall = ''
    #    string_overall += self.name
    #    return string_overall

class Purchase(SuperItem):
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

class Pickup(SuperItem):
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

class Permanent(SuperItem):
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

    def displayinfo(self, text_id):
        string_overall = ''
        string_overall += f"{self.get_name()}: "
        if text_id == 1:
            string_overall += self.get_pickup_text()
        elif text_id == 2:
            string_overall += self.get_inventory_text()
        return string_overall

class Wallet(SuperItem):
    def __init__(self, name, itemtype, pickuptext, inventorytext):
        SuperItem.__init__(self, name, itemtype, pickuptext, inventorytext)

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

class Room:
    def __init__(self, name, description, exits, unlockable_exit, items, time, hydration):
        self.name = name
        self.description = description
        self.exits = exits
        self.unlockable_exit = unlockable_exit
        self.items = items
        self.time = time
        self.hydration = hydration

    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    def get_exits(self):
        return self.exits

    def list_exits(self):
        string_exits = ""
        for i in self.get_exits():
            string_exits += f"{i}, "
        string_exits = string_exits[:-2]
        return string_exits

    def get_unlockable_exit(self):
        return self.unlockable_exit

    def update_exits(self):
        for i in range(len(self.unlockable_exit)):
            self.get_exits().append(self.unlockable_exit[i])
        self.get_unlockable_exit().clear()
        return self.exits

    def get_items(self):
        return self.items
    
    def get_time(self):
        #self.time -= 10
        return self.time
        
    def get_hydration(self):
        return self.hydration

    def list_items(self):
        string_items = ""
        for i in self.get_items():
            string_items += f"{i}, "
        string_items = string_items[:-2]
        return string_items

    def add_items(self, item_to_add):
        self.get_items().append(item_to_add)
        return self.items

    def update_items(self, item_to_remove):
        self.get_items().remove(item_to_remove)
        return self.items

    def __str__(self):
        string_overall = ""
        string_overall += f"{self.get_name()}: "
        string_overall += f"{self.get_description()}\n\n"
        string_overall += f"Exits: {self.list_exits()}\n"
        string_overall += f"Items in room: {self.list_items()}"
        #string_overall += f"You have {self.get_time()} minutes before your parents get home\n"
        #string_overall += f"Your current hydration level is {self.get_hydration()}\n"
        return string_overall


def main():
    adventure_map = AdventureMap()
    current_status = PlayerStatus()
    #room: name, description, [exits], [unlockable exits], [items], time, hydration
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

    #time_left = 300
    money_left = 0
    purchase_count = 0
    #total_money = 0
    #item: name, pickup, interact

    item_tracker = ItemTracker()
    item_tracker.add_item(Purchase('Gas Can','Purchase Item','You attempt to purchase a can of gas for $5.','It is a can of gas.'))
    item_tracker.add_item(Purchase('Air Filter', 'Purchase Item', 'You attempt to purchase an air filter for $5.','It is an air filter.'))
    item_tracker.add_item(Purchase('Boba Tea', 'Purchase Drink', 'You attempt to purchase a boba tea for $5.', 'You drink the boba tea, and feel refreshed.'))
    item_tracker.add_item(Purchase('Coffee', 'Purchase Drink', 'You attempt to purchase a coffee for $5.', 'You drink the coffee, and feel energized.'))
    item_tracker.add_item(Pickup('Keys', 'Pickup', 'You have picked up a key chain.', 'It is a key chain.'))
    item_tracker.add_item(Pickup('Credit Card', 'Pickup', 'You take your parents credit card.', 'You wonder if your parents will notice you took it. Oh well, you are going to use it for all your purchases. Surely it will be fine.'))
    item_tracker.add_item(Pickup('Gas Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the gas station.'))
    item_tracker.add_item(Pickup('Filter Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the hardware store.'))
    item_tracker.add_item(Pickup('Boba Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the boba shop.'))
    item_tracker.add_item(Pickup('Coffee Receipt', 'Pickup Receipt', 'You pick up a receipt', 'It is a record of your purchase at the coffee shop.'))
    item_tracker.add_item(Wallet('Wallet', 'Pickup', 'You pick up your wallet. It has $10 in it as well as your license.', 'It is a wallet with your license and $'))
    item_tracker.add_item(Permanent('Mower', 'Permanent', 'You try to start the mower, but nothing happens. Maybe it needs something.','You fill the mower with gas and replace the air filter, and it starts! Congratulations, better start mowing.'))
    item_tracker.add_item(Permanent('Grab Water', 'Permanent', 'You take a water bottle from the fridge.', 'You already have one, so what are you doing?'))
    item_tracker.add_item(Pickup('Note', 'Pickup', 'It is a note that says, "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We will be back at 4pm, so get moving!"', 'The note says, "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We will be back at 4pm, so get moving!"'))
    item_tracker.add_item(Pickup('Water Bottle', 'Pickup Drink', '', 'You drink the water. Gotta stay hydrated.'))
    item_tracker.add_item(Pickup('Stale Water', 'Instant Drink', 'You drink the stale water. Better than nothing.', ''))

    #would you like to purchase: purchase iff: gas can, air filter, boba tea, coffee
    # gas can added to inventory
    #iff wallet, moneyleft+10, iff credit card, moneyleft+2000
    #   you purchase x
    #   you do not have enough money
    #   you do not have enough money, so you use your parents credit card
    #thirst_text[0]:hydration_level 45+, [1]:12+, [2]:9+, [3]:6+, [4]:3+, [5]:else
    #Thirst_text = ['You get water poisoning and pass out.','You are not thirsty.', 'You are a bit thirsty.', 'You are thirsty.', 'You are very thirsty.','You pass out from dehydration.']
    #hydration_level = 9
    #status 
    
    print("Welcome to Mow the Lawn! Do your best to mow the lawn today.\n")
    logger.info("Welcome to Mow the Lawn! Do your best to mow the lawn today.\n")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("You wake up in your room. Next to you there is a note on the table next to the bed, as well as a cup of room-temperature water. It's currently noon, and you're feeling a bit thirsty.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    current_inventory = []
    current_room = 'Bedroom'
    print(adventure_map.get_room(current_room))
    string_inventory = ""
    for i in current_inventory:
        string_inventory += f"{i}, "
    string_inventory = string_inventory[:-2]
    print(f'Items in inventory: {string_inventory}\n')
    logger.info(f'Items in inventory: {string_inventory}\n')
    current_status.update_time(adventure_map.get_room(current_room).get_time())
    current_status.update_hydration(adventure_map.get_room(current_room).get_hydration())
    print(current_status)
    logger.info(current_status)
    logger.info(f'{current_status.get_hydration()} is your water level.')
    # print('\nWhat would you like to do?')
    #if player types room name, update current room, loop
    #if player types room item name, print item pickup line, loop
    #   room.update item, also room.update exits
    #if player types inventory item name, print item interact line, loop
    #   buncha if statements :')
    mowed_front = 0
    mowed_back = 0
    Continue = True
    while Continue == True:
        if current_status.get_hydration() <= 0 or current_status.get_hydration() >= 44: 
            print('Game over.')
            exit()
            logger.info('Game over.')
        elif current_status.get_time() <= 0:
            print("You ran out of time. Your parents are pulling into the driveway. Expect to be grounded for the next two weeks.")
            print('Game over.')
            exit()
            logger.info("You ran out of time. Your parents are pulling into the driveway. Expect to be grounded for the next two weeks.")
            logger.info('Game over.')
        elif (mowed_back + mowed_front == 2):
            #print(purchase_count)
            if 'Credit Card' in current_inventory and purchase_count != 0:
                print('Congrats, you have mowed the lawn. However, you were immediately grounded when they found you took their credit card and were not able to prove what you spend it on.')
                print('You lost, do better next time and maybe your parents will be proud of you.')
                logger.info('Congrats, you have mowed the lawn. However, you were immediately grounded when they found you took their credit card and were not able to prove what you spend it on.')
                logger.info('You lost, do better next time and maybe your parents will be proud of you.')
            elif 'Credit Card' in current_inventory and purchase_count == 0:
                print('Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.')
                print('You win, but maybe things could have gone a little better.')
                logger.info('Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.')
                logger.info('You win, but maybe things could have gone a little better.')
            elif current_status.get_time() >= 60:
                print('Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.')
                print('You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.')
                print('Good job! Keep it up.')
                logger.info('Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.')
                logger.info('You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.')
                logger.info('Good job! Keep it up.')
            else:
                print('Congrats, you have mowed the lawn! Your parents are very happy.')
                print('You Won!')
                logger.info('Congrats, you have mowed the lawn! Your parents are very happy.')
                logger.info('You Won!')
            exit()

        print('\nWhat would you like to do?')
        tempchoice = input()
        Choice = tempchoice.title().strip()
        logger.info(f'User input is {tempchoice} -> {Choice}.')

        try:
            if (Choice not in adventure_map.get_room(current_room).get_exits()) and (Choice not in adventure_map.get_room(current_room).get_items()) and (Choice not in current_inventory):
                raise NotFoundError(Choice)
            if Choice in adventure_map.get_room(current_room).get_exits():
                if current_room == 'Gas Station' or current_room == 'Hardware Store' or current_room == 'Boba Shop' or current_room == 'Coffee Shop':
                    if Choice == 'Garage' and 'Wallet' not in current_inventory:
                        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print('You got pulled over at a traffic stop on the way home and were found to be driving without a license.')
                        print('You did not pass go and did not collect 200 dollars, and were sent directly to jail.')
                        print('Game Over.')
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        break
                if Choice == 'Mow Front':
                    mowed_front = 1
                elif Choice == 'Mow Back':
                    mowed_back = 1
                current_room = Choice
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(adventure_map.get_room(current_room))
                string_inventory = ""
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                current_status.update_time(adventure_map.get_room(current_room).get_time())
                current_status.update_hydration(adventure_map.get_room(current_room).get_hydration())
                print(current_status)
                logger.info(current_status)
                logger.info(f'{current_status.get_hydration()} is your water level.')
                

            elif Choice in adventure_map.get_room(current_room).get_items():
                item_success = True
                if Choice == 'Wallet':
                    money_left += 10
                    #total_money += 10
                    #adventure_map.get_room(current_room).add_items("testy guy")
                #elif Choice == 'Credit Card':
                    #total_money += 2000
                elif Choice == 'Boba Tea' or Choice == 'Coffee' or Choice == 'Gas Can' or Choice == 'Air Filter':
                    if money_left >= 5:
                        money_left -= 5
                        item_success = True
                    elif 'Credit Card' in current_inventory:
                        item_success = True
                    #    total_money -= 5
                    #elif total_money >= 5:
                    #    total_money -= 5
                    else:
                        item_success = False
                    if item_success == True:
                        purchase_count += 1
                        if Choice == 'Boba Tea':
                            adventure_map.get_room(current_room).add_items("Boba Receipt")
                        elif Choice == 'Coffee':
                            adventure_map.get_room(current_room).add_items("Coffee Receipt")
                        elif Choice == 'Gas Can':
                            adventure_map.get_room(current_room).add_items("Gas Receipt")
                        elif Choice == 'Air Filter':
                            adventure_map.get_room(current_room).add_items("Filter Receipt")
                elif Choice == 'Keys':
                    adventure_map.get_room('Car').update_exits()
                    logger.info('New exits have been added to the car.')
                
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if item_success == False:
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    print("You cannot afford this item. Go search the house for some change?")
                elif Choice == 'Mower':
                    if 'Gas Can' in current_inventory and 'Air Filter' in current_inventory:
                        print(item_tracker.get_item(Choice).displayinfo(2))
                        adventure_map.get_room('Garage').update_exits()
                        logger.info('New exit has been added to the garage.')
                        #clicking on the mower starts it if you have the required items
                    else:
                        print(item_tracker.get_item(Choice).displayinfo(1))
                        #you cannot put the mower in your inventory
                elif Choice == 'Stale Water':
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    current_status.update_hydration(-5)
                    adventure_map.get_room(current_room).update_items(Choice)
                    #stale water cannot be put in inventory so it gets immediately drinkened
                    #but it does disappear from da room
                elif Choice == 'Grab Water':
                    if 'Water Bottle' not in current_inventory:
                        print(item_tracker.get_item(Choice).displayinfo(1))
                        current_inventory.append('Water Bottle')
                        #you cannot put water bottles in your in inventory, only 1 water bottle
                        #water bottles does not disappear from da room
                    else:
                        print(item_tracker.get_item(Choice).displayinfo(2))
                elif Choice == 'Wallet':
                    print(item_tracker.get_item(Choice).displayinfo(1, money_left))
                    adventure_map.get_room(current_room).update_items(Choice)
                    current_inventory.append(Choice)
                else:
                    print(item_tracker.get_item(Choice).displayinfo(1))
                    adventure_map.get_room(current_room).update_items(Choice)
                    current_inventory.append(Choice)
                    #every other item goes in your inventory
                
                if item_tracker.get_item(Choice).get_item_type() == 'Pickup Receipt':
                    purchase_count -= 1
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(adventure_map.get_room(current_room))
                string_inventory = ""
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                #current_status.update_time(adventure_map.get_room(current_room).get_time())
                #current_status.update_hydration(adventure_map.get_room(current_room).get_hydration())
                print(current_status)
                # print('\nWhat would you like to do?')
                logger.info(current_status)
                logger.info(f'{current_status.get_hydration()} is your water level.')

            elif Choice in current_inventory:
                print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if Choice == 'Wallet':
                    print(item_tracker.get_item(Choice).displayinfo(2, money_left))
                elif item_tracker.get_item(Choice).get_item_type() == 'Purchase Drink' or item_tracker.get_item(Choice).get_item_type() == 'Pickup Drink':
                    print(item_tracker.get_item(Choice).displayinfo(2))
                    current_inventory.remove(Choice)
                    current_status.update_hydration(-15)
                else:
                    print(item_tracker.get_item(Choice).displayinfo(2))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(adventure_map.get_room(current_room))
                string_inventory = ""
                for i in current_inventory:
                    string_inventory += f"{i}, "
                string_inventory = string_inventory[:-2]
                print(f'Items in inventory: {string_inventory}\n')
                logger.info(f'Items in inventory: {string_inventory}\n')
                #current_status.update_time(adventure_map.get_room(current_room).get_time())
                #current_status.update_hydration(adventure_map.get_room(current_room).get_hydration())
                print(current_status)
                logger.info(current_status)
                logger.info(f'{current_status.get_hydration()} is your water level.')
                
        except NotFoundError:
            print(NotFoundError(Choice))
            logger.warning(NotFoundError(Choice))

#STILL TO DO:
#FIX THE LOGS !!!!!!!!!
#also clear out log file
#also fix comments
#make sure we got a readme


if __name__ == "__main__":
    main()