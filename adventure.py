"""CSC111 Project 1: Text Adventure Game

Instructions (READ THIS FIRST!)
===============================

This Python module contains the code for Project 1. Please consult
the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""

from game_data import World, Item, Location, Player
from enhancement import hangman, higher_lower

def do_action(w: World, p: Player, location: Location, choice: str) -> None:
    """
    Helper function for facilitating the movement of the player in the game
    """
    print("Press 'N' for North, 'S' for South, 'E' for East, 'W' for West")
    print("You can go to the following directions: ")
    for i in location.possible_movements:
        print(i)
    direction = input("Select where you want to go ")
    if direction not in location.possible_movements:
        print("Cannot go that way, please pick a valid direction.")
        direction = input("Select where you want to go ")
    if direction == "N":
        p.y -= 1
    elif direction == "S":
        p.y += 1
    elif direction == "E":
        p.x += 1
    else:
        p.x -= 1

    p.score += location.points


if __name__ == "__main__":
    with (open("gerstein first floor.txt") as map_start, open("locations_gerstein_1F.txt") as locations_start, open(
            "items.txt") as items, open("gerstein one-below.txt") as map_1B, open("locations_gerstein_onebelow.txt")
            as location_1B, open("innis ground floor.txt") as ground_floor, open("locations_innis_ground_floor.txt")
            as location_gf_innis, open("innis study room.txt") as map_study, open("locations_innis_study_room.txt") as
            location_study, open("innis suite.txt") as map_suite, open("locations_innis_suite.txt") as location_suite):
        w_start = World(map_start, locations_start, items)
        items.close()
        items = open("items.txt")
        w_gerstein_1B = World(map_1B, location_1B, items)
        items.close()
        items = open("items.txt")
        w_innis_gf = World(ground_floor, location_gf_innis, items)
        items.close()
        items = open("items.txt")
        w_innis_study = World(map_study, location_study, items)
        items.close()
        items = open("items.txt")
        w_innis_suite = World(map_suite, location_suite, items)

        p = Player(1, 3)  # set starting location of player; you may change the x, y coordinates here as appropriate

        menu = ["Go", "look", "inventory", "score", "quit", "back", "take", "remove"]

        curr_world = w_start

        print("Last night, you were studying for your exam today. You went to gerstein Library to study during the day "
              "and then came back home in the evening and studied with your friend in her room untill late night. "
              "However, today morning when you woke up, and were going to go to library to study for the exam, you "
              "realize you have lost your T-card, Cheat Sheet and your lucky pen! Where could have lost these items. "
              "You will start your search from Gerstein library and continue from there. Remeber that any item you "
              "pick up during the game has points associated with it so if you pick an item that needs to be put back "
              "at its original place and do not put it back at its place by the end of game, points will be deducted!")

        game_played_cheatsheet = False
        game_played_pen = False
        new_lst = ["t-card", "pen", "cheatsheet"]
        p.moves = 100
        while not p.victory and p.moves != 0:
            location = curr_world.get_location(p.x, p.y)

            if location.num == 21:
                if curr_world == w_start and location.visited:
                    curr_world = w_innis_gf
                    location = curr_world.location[21]
                    p.x = location.position[0]
                    p.y = location.position[1]
                    print("You are now at Innis College Residence ground floor")
                elif curr_world == w_innis_gf and location.visited:
                    curr_world = w_start
                    location = curr_world.location[21]
                    p.x = location.position[0]
                    p.y = location.position[1]
                    print("You are now at Gerstein Library")
                elif curr_world == w_innis_study:
                    if curr_world.items["keycard"] in p.inventory:
                        curr_world = w_innis_suite
                        print("You are now in your suite")
                        location = curr_world.location[21]
                        p.x = location.position[0]
                        p.y = location.position[1]
                    else:
                        print("You do not have your friend's key card yet so you cannot enter right now")
                elif curr_world == w_innis_suite and location.visited:
                    curr_world = w_innis_study
                    location = curr_world.location[21]
                    p.x = location.position[0]
                    p.y = location.position[1]

            elif location.num == 20:
                if curr_world == w_start:
                    curr_world = w_gerstein_1B
                elif curr_world == w_innis_gf:
                    curr_world = w_innis_study
                elif curr_world == w_innis_study:
                    curr_world = w_innis_gf
                elif curr_world == w_innis_suite:
                    curr_world = w_innis_study

                p.x = curr_world.location[20].position[0]
                p.y = curr_world.location[20].position[1]
                location = curr_world.get_location(p.x, p.y)

            if not location.visited:
                print(location.full_description)
            else:
                print(location.brief_description)

            if curr_world == w_gerstein_1B and location.num == 6:
                if not game_played_cheatsheet:
                    user = input("Type 'play' to play the game")
                    if user.lower() == "play":
                        result = hangman()
                        while not result:
                            result = hangman()
                            p.moves -= 1
                        game_played_cheatsheet = True
                        item_object = curr_world.items["cheatsheet"]
                        p.inventory.append(item_object)
                        location.available_items.remove("cheatsheet")
                        p.score += item_object.target_points
                    else:
                        choice = input("\nEnter action: ")

            if curr_world == w_gerstein_1B and location.num == 4:
                if not game_played_pen:
                    user = input("Type 'play' to play the game to get your lucky pen")
                    if user.lower() == "play":
                        result = higher_lower()
                        while result != True:
                            result = higher_lower()
                            p.moves -= 1
                        game_played_pen = True
                        pen_object = curr_world.items["pen"]
                        p.inventory.append(pen_object)
                        location.available_items.remove("pen")
                        p.score += pen_object.target_points
                    else:
                        choice = input("\nEnter action: ")

            # Depending on whether or not it's been visited before,
            # print either full description (first time visit) or brief description (every subsequent visit)
            # print("Gerstein description and back story")

            print("What to do? \n")
            print("[menu]")

            choice = input("\nEnter action: ")

            if choice == "[menu]":
                print("Menu Options: \n")
                for option in menu:
                    print(option)
                choice = input("\nChoose action: ") + ''

            if choice.lower() == "go":
                do_action(w_start, p, location, choice)
                location.visited = True
            elif choice.lower() == "look":
                print(location.full_description)
                choice = input("\nChoose action: ") + ''
            elif choice.lower() == "inventory":
                for i in p.inventory:
                    print(i.name)
                choice = input("\nChoose action: ") + ''

            elif choice.lower() == "score":
                print(p.score)
                choice = input("\nChoose action: ") + ''

            elif choice.lower() == "take" or choice.lower() == "remove":
                item = input("What would you like to take or remove? ")
                while item.lower() not in curr_world.items:
                    print("Please enter a valid item")
                    item = input("What would you like to take or remove? ")
                obj = curr_world.items[item.lower()]
                p.update_inventory(choice, obj, location, game_played_cheatsheet, game_played_pen)
                if item == "t-card":
                    location.available_items.remove("t-card")

                choice = input("\nChoose action: ") + ''
            elif choice.lower() == "quit":
                break
            lst = []
            for i in p.inventory:
                lst.append(i.name)
            if lst == new_lst:
                p.victory = True
            p.moves -= 1

            # TODO: CALL A FUNCTION HERE TO HANDLE WHAT HAPPENS UPON THE PLAYER'S CHOICE
            #  REMEMBER: the location = w.get_location(p.x, p.y) at the top of this loop will update the location if
            #  the choice the player made was just a movement, so only updating player's position is enough to change the
            #  location to the next appropriate location
            #  Possibilities:
            #  A helper function such as do_action(w, p, location, choice)
            #  OR A method in World class w.do_action(p, location, choice)
            #  OR Check what type of action it is, then modify only player or location accordingly
            #  OR Method in Player class for move or updating inventory
            #  OR Method in Location class for updating location item info, or other location data etc....

    if p.victory:
        print("Wohoooo, You won! Good luck on your exam!!")
    else:
        print("Oh no! Better luck next time!")



