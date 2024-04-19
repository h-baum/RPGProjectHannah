"""
Author:         Hannah Baum
Date:           4/1/24
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    SECTION 002

CODE DESCRIPTION: 


"""




class ExitNotFoundError(Exception):
    def __init__(self, room_name, message = "Room or Item not found"):
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

class Room:
    def __init__(self, name, description, exits, items, time, hydration):
        self.name = name
        self.description = description
        self.exits = exits
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
            string_exits += f"{i}\n"
        return string_exits
    
    def get_items(self):
        return self.items
    
    def get_time(self):
        #self.time -= 10
        return self.time

    def update_time(self):
        #if self.name not in ["Side-Yard", "Back-Yard", "Front-Yard"]:
         #   self.get_time(self) -= 10
        #else:
         #   self.get_time(self) -= 100
        #return self.time
        pass
        
    def get_hydration(self):
        return self.hydration

    def update_hydration(self, drink):
        return self.hydration

    def list_items(self):
        string_items = ""
        for i in self.get_items():
            string_items += f"{i}\n"
        return string_items

    def update_items(self, item_to_remove):
        self.get_items().remove(item_to_remove)
        return self.items

    def __str__(self):
        string_overall = ""
        string_overall += f"{self.get_name()}: "
        string_overall += f"{self.get_description()}\n\n"
        string_overall += f"Exits:\n{self.list_exits()}\n"
        string_overall += f"Time left is {self.get_time()} minutes\n"
        string_overall += f"Hydration level is {self.get_hydration()}\n"
        return string_overall


def main():
    adventure_map = AdventureMap()
    time = 600

    adventure_map.add_room(Room("Bedroom", "A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?", ['Kitchen', 'Parent\'s Room'], ["Note", "Wallet"],time - 10, ""))
    adventure_map.add_room(Room("Kitchen", "A room with a leaky sink and an empty fridge.", ['Garage', 'Parent\'s Room', 'Bedroom'], [], time-10, ""))
    adventure_map.add_room(Room("Parent's Room", "A fresh clean room. The beds are nicely made, the clothes are folded and put away. Maybe you could take some hints?", ['Kitchen', 'Bedroom'], ["Parent_Wallet"], time - 10, ""))
    adventure_map.add_room(Room("Garage", "There's a car parked up front. There's some tools and ladders against the walls.", ['Gas Station', 'Starbucks', 'Boba Shop', 'Back-Yard'], ["Gas_Can", "Car", "Mower", "Bug_Spray"], time-10, ""))
    adventure_map.add_room(Room("Boba Shop", "A shop stocked with all the delicious boba drinks you could imagine!!!", ['Garage', 'Starbucks', 'Gas Station'], ["Car"], time-10, ""))
    adventure_map.add_room(Room("Starbucks", "A shop stocked with many caffeinated drinks. Could caffeine be useful?", ['Garage', 'Boba Shop', 'Gas Station'],["Car"], time-10, ""))
    adventure_map.add_room(Room("Gas Station", "A store containing gas for your lawn mower", ['Garage', 'Boba Shop', 'Starbucks'], ["Car"], time-10, ""))
    adventure_map.add_room(Room("Back-Yard", "Your parents have a big yard. Maybe they should consider downsizing?", ['Garage', 'Side-Yard', 'Front-Yard'], [], time-10, ""))
    adventure_map.add_room(Room("Front-Yard", "There's a mysterious hole in the ground", ['Back-Yard', 'Side-Yard'], [], time-10, ""))
    adventure_map.add_room(Room("Side-Yard", "Almost done mowing!!!", ['Back-Yard', 'Front-Yard'], [], time-10, ""))

    my_funds = 0
    parent_funds = 0
    current_gas = 0
#    Item_List = [[item, text when you add item to inventory, interact text1, interact text2]]
    Item_List = [["Note", "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We'll be back at 6, so get moving!", ""], 
                ["Wallet", "You pick up your wallet. You have $10 available.", f"You have ${my_funds} available."],
                ["Parent's Wallet", "You pick up your parent's wallet. You have $100 available.",f"You have ${parent_funds} available."],
                ["Gas Can", "You have picked up the gas can. It is empty.", f"You have {current_gas} available."],
                ["Car", "You have entered the car.", "The car is locked and you have no keys."],
                ["Keys", "You have picked up a pair of keys.", "You have a pair of keys."],
                ["Mower", "It is a mower that has not been used since last year. It has no gas in it.", "It is a mower that has recently been filled with gas."]]

        #    ["Spark Plug", "You have purchased a spark plug.", "You cannot afford a spark plug.", "You have a spark plug."],

# Have an outer loop of whether you want to play again
# every turn print room description, hydration, time, funds?, exits, items in room, items in inventory
    print("Welcome to Mow the Lawn!")
    print("You wake up in your room. Next to you there is note on the table next to the bed. It's currently noon. What would you like to do?")
    room_name = "Bedroom"
    print(adventure_map.get_room(room_name))
    Note = "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We'll be back at 6, so get moving!"
    Continue = "yes"
    My_Wallet = 15
    Parent_Wallet = 100
    Time_left = 600
    while Continue == "yes":
        Choice = input()
        Choice = Choice.title()
        if Choice == "pick up note":
            print(Note)
            print('What do you want to do now?')
            Choice = input().title()
        else:
            room_name = Choice
            #if room_name not in adventure_map.get_room(Choice).list_exits():
                # raise the exception class
             #   raise ExitNotFoundError(room_name)
            print(adventure_map.get_room(room_name))
            print("Where do you want to go now?")
            #if room_name == "Bedroom":
            #    Time_left -= 10
            #    print(f"You have {Time_left} minutes before parents come home")
            if room_name == "Boba Shop":
                menu = {"lychee juice": 10, "oolong milk tea": 10, "taro milk tea": 10, "pineapple tea": 10, "nothing": 0}
                print(f"Your options are {menu}")
                print("What would you like to order")
                order = input()
                if order == "pineapple tea":
                    print("You are severely allergic to pineapple. You died.")
                    exit()
                else:
                    print("Are you using your parent's money or your money?")
                    print('Options are Mine or Theirs')
                    Money = input()
                    if Money == "Mine":
                        My_Wallet -= menu[order]
                    elif Money == "Theirs":
                        Parent_Wallet -= menu[order]
                    if My_Wallet < 0 or Parent_Wallet <= 0:
                        print(f"You tried to steal from {room_name}. Go directly to jail. Do not pass go. Do not collect $200.")
                        exit()                    
                    print(f"Thank you for your order. You paid {menu[order]} dollars")

            if room_name == "Starbucks":
                menu = {"iced latte": 10, "pink drink": 10, "pineapple dragonfruit refresher": 15, "expresso": 5, "cappuccino": 8, "nothing": 0}
                print(f"Your options are {menu}")
                print("What would you like to order")
                order = input()
                if order == "mango dragonfruit refresher":
                    print("You are severely allergic to mango. You died.")
                    exit()
                else:
                    print("Are you using your parent's money or your money?")
                    print('Options are Mine or Theirs')
                    Money = input()
                    if Money == "Mine":
                        My_Wallet -= menu[order]
                    elif Money == "Theirs":
                        Parent_Wallet -= menu[order]
                    if My_Wallet < 0 or Parent_Wallet <= 0:
                        print(f"You tried to steal from {room_name}. Go directly to jail. Do not pass go. Do not collect $200.")
                        exit()                    
                    print(f"Thank you for your order. You paid {menu[order]} dollars")

            if room_name == "Side-Yard":
                print("There's a mysterious hole in the ground. What do you want to do?")
                print("You can")
                print("(A) keep going      (B) go back to Garage    (C) wait around for a miracle to happen")
                Hole = input()
                if Hole == "A":
                    print("You mowed over a yellow jacket's nest. You were stung 100 times. You died.")
                    exit()
                elif Hole == "B":
                    room_name = "Garage"
                elif Hole == "C":
                    print("You waited and waited. And kept waiting.")
                    print("...")
                    print("...")
                    print("Well nothing happened. You just waited 3 hours!")
                    #Time += 3


            if room_name == "Gas Station":
                print("There's a sign that says (Gas costs $5 a gallon). You know that your mower holds 3 gallons.")
                Gas = 3
                print("Are you using your parent's money or your money?")
                print('Options are Mine or Theirs')
                Money = input()
                if Money == "Mine":
                    My_Wallet -= 5*Gas
                elif Money == "Theirs":
                    Parent_Wallet -= 5*Gas
                if My_Wallet < 0 or Parent_Wallet <= 0:
                        print(f"You tried to steal from {room_name}. Go directly to jail. Do not pass go. Do not collect $200.")
                        exit()
                print(f"You paid ${Gas*5}")

        if Time_left == 0 and Parent_Wallet < 100:
            print("Your parents found out you stole their money for a sweet treat. They're really mad, and you're GROUNDED for the rest of your life!!!")
            exit()

    if (My_Wallet == 0 and Parent_Wallet == 100) or (My_Wallet == 15 and Parent_Wallet == 85):
        print("You successfully mowed the lawn in time! Congrats! You win!")
        print()
        print()
        print("Maybe there's a cooler ending? What could have made your day even better?")
    else:
        print("You successfully mowed the lawn in time! Congrats! You win!")
        print("You even managed to have a sweet treat! What a perfect ending.")
        print()
        #except ExitNotFoundError:
            # print out the exception error message 
        #    print(ExitNotFoundError(room_name))
       
    print("You took so long, your parents are back now. They're very annoyed you didn't finish mowing. You're GROUNDED!!!")
# Runs main
if __name__ == "__main__":
    main()