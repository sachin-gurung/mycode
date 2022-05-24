#!/usr/bin/python3
import requests

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

#def getDirections():
  #print the directions user can go to  
  #directions = ['east', 'west', 'north', 'south']
  #actualDirections = []
  #print(f'You can turn: ')
  #if directions in rooms[currentRoom]:
    #for item in directions:
      #print(item)

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print Kanye West quotes if player is in the Bonus Room 
  if currentRoom == 'Bonus Room':
    kanyeWestQuotes()
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")  

  #if "items" in rooms[currentRoom]:
    #for item in items:
      #totalItems = items.append(item)
      #print("You see " + rooms[currentRoom][totalItems])
    #print("------------------------------")


#Implementing Kanye Rest API
def kanyeWestQuotes():
  response = requests.get("https://api.kanye.rest").json()
  quote = response["quote"]
  print(quote)
  

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Bonus Room',
                  'west' : 'Guest Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'east' : 'Garden',
                  'west' : 'Bathroom',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'north' : 'Pantry',
                  'item' : 'potion',
               },
            'Garden' : {
                  'north' : 'Dining Room',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'west' : 'Bonus Room',
                  'item' : 'cookie',
            },
            'Bonus Room' : {
                  'east' : 'Pantry',
                  'west' : 'Master Bedroom',
                  'south': 'Hall',
            },
            'Master Bedroom' : {
                  'south' : 'Guest Room',
                  'east' : 'Bonus Room',
                  'item' : 'masterkey', #['masterkey', 'diamond','tv'], # multiple items
            },
            'Guest Room' : {
                  'east' : 'Hall',
                  'south': 'Bathroom',
                  'item' : 'book',
            },
            'Bathroom' : {
                  'east' : 'Kitchen',
                  'north' : 'Guest Room',
                  'item': 'gun',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()


#loop forever
while True:

  showStatus()
  

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break
  ## If a player enters a room with a monster and player is carrying a gun
  elif 'gun' in inventory and currentRoom == 'Kitchen':
    print('You got a gun in your pocket. You shot the monster in the head. Now the monster is dead... GAME OVER!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you and you don\'t have a gun... GAME OVER!')
    break
