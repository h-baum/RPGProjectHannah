# RPGProjectHannah
This is Project2 of CPSC1050 Introduction to Programming in Python.

The game's title is Mow the Lawn

GitHub Link:    https://github.com/h-baum/RPGProjectHannah/tree/main

CODE DESCRIPTION: This code runs a text-based RPG game. The goal is to mow the lawn before your parents get home.

There are 5 ways to lose the game. You can pass out from dehydration, run out of time, drive without your wallet, drink too much and get water poisoning, or take your parents credit card and don't have all the receipts for your purchases.
There are 3 win messages. One is when you speedrun the game and make no/almost no extra moves (Best Ending), another is when you finish the game in time but make several unnecessary moves without using the credit card, and the last is when you take the credit card so you spend your parents money, and you show the receipts.

With each room you go into, the hydration, time remaining, and items in room will update. 
Inventory will only change if you add something from the room or use up something in your inventory.
Drinks go straight to your inventory when selected from the room and can be drunk (selected) at any later time in the game. 
The only exception to that is the stale water, which will be drunk immediately and serves the purpose of letting you start 
not being a little bit thirsty. It's not necessary, but it also shows you how drinking water changes your thirst level.
Any non-drink in your inventory will just read a description when you select it.

If you go to the mower without gas can and air filter, mower will not start. 
If you go to the car without keys, you can not go from your car to any of the shops.

If you are walking from room to room, it takes 10 minutes and hydration goes down by 1.
Driving from room to room takes 20 minutes, and hydration goes down by 1.
Mowing half of the lawn takes 30 minutes, and hydration goes down by 5. In total, it will take 70 minutes to go from start 
mowing to ending the game by finishing mowing both front and back.

You start the game with hydration of 10. Drinking anything increases hydration by 15, except for stale water which only 
increases hydration by 5.
You start the game with 240 minutes. 

Interacting with items in room or inventory does not decrease time or hydration, only moving rooms does. 
Mower is a permanent item in the garage, but it unlocks start mowing exit if you have the correct items in your inventory.
It is possible to pass out or run out of time as you are finishing mowing, and if that happens, you lose. 

The log file stores the number of turns, user input, time, hydration, and items in inventory.

Instructions: Your next move can be typing the name of an item in the room, an item in your inventory, or an exit.
You need to type in the actual name of the item or exit, no abbreviations or short form, but capitalization doesn't matter. 
If you type something
that is not one of those choices, it will raise an exception class that will tell you that was not a valid option
and you can reinput something.


Sample Test Cases:

Test Case 1
Normal Win with Credit Card in Inventory:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Mow the Lawn! Do your best to mow the lawn today.

You wake up in your room. Next to you there is a note on the table next to the bed, as well as a cup of room-temperature water. It's currently noon, and you're feeling a bit thirsty.
Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note, Wallet, Stale Water
Items in inventory: 

You have 240 minutes left.
You are a bit thirsty.

What would you like to do?
wallet

Wallet: You pick up your wallet. It has $10 in it as well as your license.
Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note, Stale Water
Items in inventory: Wallet

You have 240 minutes left.
You are a bit thirsty.

What would you like to do?
stale water

Stale Water: You drink the stale water. Better than nothing.

Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note
Items in inventory: Wallet

You have 240 minutes left.
You are not thirsty.

What would you like to do?
note

Note: It is a note that says, "Hi kid, we just left, and you need to mow the lawn before we get home, or you are grounded. We will be back at 4pm, so get moving!"
Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: 
Items in inventory: Wallet, Note

You have 240 minutes left.
You are not thirsty.

What would you like to do?
wallet

Wallet: It is a wallet with your license and $10 in it.
Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: 
Items in inventory: Wallet, Note

You have 240 minutes left.
You are not thirsty.

What would you like to do?
master bedroom

Master Bedroom: Your parents keep their room clean and tidy. The beds are nicely made, the clothes are folded and put away. Maybe you could take some hints?

Exits: Kitchen, Bedroom
Items in room: Credit Card
Items in inventory: Wallet, Note

You have 230 minutes left.
You are not thirsty.

What would you like to do?
credit card

Credit Card: You take your parents credit card.
Master Bedroom: Your parents keep their room clean and tidy. The beds are nicely made, the clothes are folded and put away. Maybe you could take some hints?

Exits: Kitchen, Bedroom
Items in room: 
Items in inventory: Wallet, Note, Credit Card

You have 230 minutes left.
You are not thirsty.

What would you like to do?
kitchen

Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water, Keys
Items in inventory: Wallet, Note, Credit Card

You have 220 minutes left.
You are not thirsty.

What would you like to do?
keys 

Keys: You have picked up a key chain.
Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water
Items in inventory: Wallet, Note, Credit Card, Keys

You have 220 minutes left.
You are not thirsty.

What would you like to do?
grab water

Grab Water: You take a water bottle from the fridge.
Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 220 minutes left.
You are not thirsty.

What would you like to do?
grab water

Grab Water: You already have one, so what are you doing? Don't be greedy.
Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 220 minutes left.
You are not thirsty.

What would you like to do?
garage

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car
Items in room: Mower
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 210 minutes left.
You are not thirsty.

What would you like to do?
mower

Mower: You try to start the mower, but nothing happens. Maybe it needs something.
Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car
Items in room: Mower
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 210 minutes left.
You are not thirsty.

What would you like to do?
car

Car: You get inside the vehicle. If you have keys, you can drive to many places.

Exits: Garage, Boba Shop, Coffee Shop, Gas Station, Hardware Store
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 200 minutes left.
You are not thirsty.

What would you like to do?
gas station

Gas Station: You drive to a store containing gas for your lawn mower.

Exits: Garage, Boba Shop, Coffee Shop, Hardware Store
Items in room: Gas Can
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle

You have 180 minutes left.
You are a bit thirsty.

What would you like to do?
gas can

Gas Can: You attempt to purchase a can of gas for $5.
Gas Station: You drive to a store containing gas for your lawn mower.

Exits: Garage, Boba Shop, Coffee Shop, Hardware Store
Items in room: Gas Receipt
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle, Gas Can

You have 180 minutes left.
You are a bit thirsty.

What would you like to do?
gas receipt

Gas Receipt: You pick up a receipt
Gas Station: You drive to a store containing gas for your lawn mower.

Exits: Garage, Boba Shop, Coffee Shop, Hardware Store
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle, Gas Can, Gas Receipt

You have 180 minutes left.
You are a bit thirsty.

What would you like to do?
hardware store

Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: Air Filter
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle, Gas Can, Gas Receipt

You have 160 minutes left.
You are thirsty.

What would you like to do?
air filter

Air Filter: You attempt to purchase an air filter for $5.
Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: Filter Receipt
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle, Gas Can, Gas Receipt, Air Filter

You have 160 minutes left.
You are thirsty.

What would you like to do?
filter receipt

Filter Receipt: You pick up a receipt
Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Water Bottle, Gas Can, Gas Receipt, Air Filter, Filter Receipt

You have 160 minutes left.
You are thirsty.

What would you like to do?
water bottle

Water Bottle: You drink the water. Gotta stay hydrated.
Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt

You have 160 minutes left.
You are not thirsty.

What would you like to do?
boba shop

Boba Shop: You drive to a shop stocked with all the delicious boba drinks you could imagine!!!

Exits: Garage, Coffee Shop, Gas Station, Hardware Store
Items in room: Boba Tea
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt

You have 140 minutes left.
You are not thirsty.

What would you like to do?
boba tea

Boba Tea: You attempt to purchase a boba tea for $5.
Boba Shop: You drive to a shop stocked with all the delicious boba drinks you could imagine!!!

Exits: Garage, Coffee Shop, Gas Station, Hardware Store
Items in room: Boba Receipt
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea

You have 140 minutes left.
You are not thirsty.

What would you like to do?
boba receipt

Boba Receipt: You pick up a receipt
Boba Shop: You drive to a shop stocked with all the delicious boba drinks you could imagine!!!

Exits: Garage, Coffee Shop, Gas Station, Hardware Store
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 140 minutes left.
You are not thirsty.

What would you like to do?
garage

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car
Items in room: Mower
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 130 minutes left.
You are not thirsty.

What would you like to do?
mower

Mower: You fill the mower with gas and replace the air filter, and it starts! Congratulations, better start mowing.
Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car, Start Mowing
Items in room: Mower
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 130 minutes left.
You are not thirsty.

What would you like to do?
start mowing

Start Mowing: You successfully start the mower.

Exits: Mow Front, Mow Back, Garage
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 120 minutes left.
You are not thirsty.

What would you like to do?
mow front

Mow Front: You mow the front yard.

Exits: Mow Back, Garage
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 90 minutes left.
You are not thirsty.

What would you like to do?
mow back

Mow Back: You mow the back yard.

Exits: Mow Front, Garage
Items in room: 
Items in inventory: Wallet, Note, Credit Card, Keys, Gas Can, Gas Receipt, Air Filter, Filter Receipt, Boba Tea, Boba Receipt

You have 60 minutes left.
You are a bit thirsty.

Congrats, you have mowed the lawn. While your parents were not happy with you for taking their card, you were able to calm them down when you showed them the receipts for your purchases.
You win, but maybe things could have gone a little better.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Test Case 2
Win with Best Ending:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Mow the Lawn! Do your best to mow the lawn today.

You wake up in your room. Next to you there is a note on the table next to the bed, as well as a cup of room-temperature water. It's currently noon, and you're feeling a bit thirsty.

Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note, Wallet, Stale Water
Items in inventory: 

You have 240 minutes left.
You are a bit thirsty.

What would you like to do?
wallet

Wallet: You pick up your wallet. It has $10 in it as well as your license.

Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note, Stale Water
Items in inventory: Wallet

You have 240 minutes left.
You are a bit thirsty.

What would you like to do?
stale wter
Stale Wter -> Room or Item not found. Please try again.

What would you like to do?
stale water

Stale Water: You drink the stale water. Better than nothing.

Bedroom: A messy room that desparately needs organizing and cleaning. At least nothing is growing, I think?

Exits: Kitchen, Master Bedroom
Items in room: Note
Items in inventory: Wallet

You have 240 minutes left.
You are not thirsty.

What would you like to do?
kitchen

Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water, Keys
Items in inventory: Wallet

You have 230 minutes left.
You are not thirsty.

What would you like to do?
keys 

Keys: You have picked up a key chain.

Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water
Items in inventory: Wallet, Keys

You have 230 minutes left.
You are not thirsty.

What would you like to do?
grab water

Grab Water: You take a water bottle from the fridge.

Kitchen: A room with a leaky sink and an near-empty fridge, containing only several water bottles.

Exits: Garage, Master Bedroom, Bedroom
Items in room: Grab Water
Items in inventory: Wallet, Keys, Water Bottle

You have 230 minutes left.
You are not thirsty.

What would you like to do?
garage

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car
Items in room: Mower
Items in inventory: Wallet, Keys, Water Bottle

You have 220 minutes left.
You are not thirsty.

What would you like to do?
car

Car: You get inside the vehicle. If you have keys, you can drive to many places.

Exits: Garage, Boba Shop, Coffee Shop, Gas Station, Hardware Store
Items in room: 
Items in inventory: Wallet, Keys, Water Bottle

You have 210 minutes left.
You are not thirsty.

What would you like to do?
gas station

Gas Station: You drive to a store containing gas for your lawn mower.

Exits: Garage, Boba Shop, Coffee Shop, Hardware Store
Items in room: Gas Can
Items in inventory: Wallet, Keys, Water Bottle

You have 190 minutes left.
You are a bit thirsty.

What would you like to do?
gas can

Gas Can: You attempt to purchase a can of gas for $5.

Gas Station: You drive to a store containing gas for your lawn mower.

Exits: Garage, Boba Shop, Coffee Shop, Hardware Store
Items in room: Gas Receipt
Items in inventory: Wallet, Keys, Water Bottle, Gas Can

You have 190 minutes left.
You are a bit thirsty.

What would you like to do?
hardware store

Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: Air Filter
Items in inventory: Wallet, Keys, Water Bottle, Gas Can

You have 170 minutes left.
You are a bit thirsty.

What would you like to do?
air filter

Air Filter: You attempt to purchase an air filter for $5.

Hardware Store: You drive to a store containing air filters for your lawn mower.

Exits: Garage, Gas Station, Boba Shop, Coffee Shop
Items in room: Filter Receipt
Items in inventory: Wallet, Keys, Water Bottle, Gas Can, Air Filter

You have 170 minutes left.
You are a bit thirsty.

What would you like to do?
garage

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car
Items in room: Mower
Items in inventory: Wallet, Keys, Water Bottle, Gas Can, Air Filter

You have 160 minutes left.
You are thirsty.

What would you like to do?
mower

Mower: You fill the mower with gas and replace the air filter, and it starts! Congratulations, better start mowing.

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car, Start Mowing
Items in room: Mower
Items in inventory: Wallet, Keys, Water Bottle, Gas Can, Air Filter

You have 160 minutes left.
You are thirsty.

What would you like to do?
water bottle

Water Bottle: You drink the water. Gotta stay hydrated.

Garage: There's a car parked in the garage. There's some tools, ladders, and cobwebs against the walls.

Exits: Kitchen, Front Yard, Back Yard, Car, Start Mowing
Items in room: Mower
Items in inventory: Wallet, Keys, Gas Can, Air Filter

You have 160 minutes left.
You are not thirsty.

What would you like to do?
start mowing

Start Mowing: You successfully start the mower.

Exits: Mow Front, Mow Back, Garage
Items in room: 
Items in inventory: Wallet, Keys, Gas Can, Air Filter

You have 150 minutes left.
You are not thirsty.

What would you like to do?
mow front

Mow Front: You mow the front yard.

Exits: Mow Back, Garage
Items in room: 
Items in inventory: Wallet, Keys, Gas Can, Air Filter

You have 120 minutes left.
You are not thirsty.

What would you like to do?
mow back

Mow Back: You mow the back yard.

Exits: Mow Front, Garage
Items in room: 
Items in inventory: Wallet, Keys, Gas Can, Air Filter

You have 90 minutes left.
You are not thirsty.

Congrats, you have mowed the lawn! Your parents were impressed with your speed and decided to reward you by paying for your next boba.
You immediately went to the boba shop and bought yourself a lychee-flavored boba tea. Maybe it was worth doing your best for your parents.
Good job! Keep it up.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
