"""CSC111 Project 1: Text Adventure Game Classes

Instructions (READ THIS FIRST!)
===============================

This Python module contains the main classes for Project 1, to be imported and used by
 the `adventure` module.
 Please consult the project handout for instructions and details.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2024 CSC111 Teaching Team
"""
from typing import Optional, TextIO
import ast


class Location:
    """A location in our text adventure game world.

    Instance Attributes:
        - num: number associated with the location
        - full_description: entire description of a particular location
        - breif_description: a shorter description of a particular location
        - available_items: what items can the player find at a particular location
        - visited: checks whether the place has been visited before

    Representation Invariants:
        -
    """

    num: int
    position: tuple[int, int]
    points: int
    full_description: str
    breif_description: str
    available_items: list[str]
    visited: bool
    possible_movements: list[str]

    def __init__(self, num: int, position: tuple[int, int], points: int, full_description: str, brief_description: str, available_items: list[str], possible_movements: list[str]) -> None:
        """Initialize a new location.

        # TODO Add more details here about the initialization if needed
        """

        # NOTES:
        # Data that could be associated with each Location object:
        # a position in the world map,
        # a brief description,
        # a long description,
        # a list of available commands/directions to move,
        # items that are available in the location,
        # and whether the location has been visited before.
        # Store these as you see fit, using appropriate data types.
        #
        # This is just a suggested starter class for Location.
        # You may change/add parameters and the data available for each Location object as you see fit.
        #
        # The only thing you must NOT change is the name of this class: Location.
        # All locations in your game MUST be represented as an instance of this class.

        self.num = num
        self.position = position
        self.points = points
        self.full_description = full_description
        self.brief_description = brief_description
        self.available_items = available_items
        self.visited = False
        self.possible_movements = possible_movements


class Item:
    """An item in our text adventure game world.

    Instance Attributes:
        - name: name of the item
        - start_world: name of the world that this item is in
        - target_world: name of the world that this items needs to be deposited at
        - start_position: the location of where the item was originally found
        - target_position: the location of where the item is supposed to be placed
        - target_points: the number of points allocated for picking up an item

    Representation Invariants:
        - start_position != -1
        - target_position != -1
        - target_points >= 0
    """
    name: str
    start_world: str
    target_world: str
    start_position: int
    target_position: int
    target_points: int

    def __init__(self, name: str, start: int, world: str, target_world: str, target_position: int, target_points: int) -> None:
        """Initialize a new item.
        """

        # NOTES:
        # This is just a suggested starter class for Item.
        # You may change these parameters and the data available for each Item object as you see fit.
        # (The current parameters correspond to the example in the handout).
        # Consider every method in this Item class as a "suggested method".
        #
        # The only thing you must NOT change is the name of this class: Item.
        # All item objects in your game MUST be represented as an instance of this class.
        # New comment

        self.name = name
        self.start_world = world
        self.target_world = target_world
        self.target_position = target_position
        self.start_position = start
        self.target_points = target_points


class Player:
    """
    A Player in the text advanture game.

    Instance Attributes:
        - x : x-corrdinate of the player's current location
        - y: y-coordinate of the player's current location
        - inventory: list of items
        - victory: stores whether the player has won or not. Intialized to False at the beginning of the game

    Representation Invariants:
        - x >= 0 and y >= 0
        -

    """

    x: int
    y: int
    inventory: list[Item]
    victory: bool
    score: int
    moves: int

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes a new Player at position (x, y).
        """

        # NOTES:
        # This is a suggested starter class for Player.
        # You may change these parameters and the data available for the Player object as you see fit.

        self.x = x
        self.y = y
        self.inventory = []
        self.victory = False
        self.score = 0
        self.moves = 0

    def add_points(self, item: Item, location: Location) -> None:
        """
        Helper function to give the player points only if he/she manages to deposit the item back
        to its plae if it was meant to be. Otherwise deduct points for removing an item that was not
        to be removed or if it was removed at the wrong location.
        """
        if item.target_position == item.start_position:
            if location == item.target_position:
                self.score += item.target_points
            else:
                self.score -= item.target_points

    def update_inventory(self, choice: str, item: Item, location: Location, game_cheatsheet: bool, game_pen: bool) -> None:
        if choice.lower() == "take":
            if item.name in location.available_items:
                if (item.name == "cheatsheet" and game_cheatsheet or item.name == "pen" and game_pen or
                        item.name != "cheatsheet" or "pen"):
                    self.inventory.append(item)
                else:
                    print("You cannot take this item just yet!")
            else:
                print("This item is not available in present in this location")
        elif choice.lower() == "remove":
            if item in self.inventory:
                for items in self.inventory:
                    if items.name == item.name:
                        self.inventory.remove(item)
            else:
                print("This item is not in your inventory, you cannot implement this action.")

            self.add_points(item, location)

class World:
    """A text adventure game world storing all location, item and map data.

    Instance Attributes:
        - map: a nested list representation of this world's map
        - location: a dictionary containing the locations avaiable with each of its corresponding informations
        - items: a dictionary conatining the items available with each of its corresponding informations

    Representation Invariants:
        - self.map != []
        - self.location != {}
        - self.itesm != {}
    """
    map = list[list[int]]
    location: dict[int: Location]
    items: dict[str: Item]

    def __init__(self, map_data: TextIO, location_data: TextIO, items_data: TextIO) -> None:
        """
        Initialize a new World for a text adventure game, based on the data in the given open files.

        - location_data: name of text file containing location data (format left up to you)
        - items_data: name of text file containing item data (format left up to you)
        """

        # NOTES:

        # map_data should refer to an open text file containing map data in a grid format, with integers separated by a
        # space, representing each location, as described in the project handout. Each integer represents a different
        # location, and -1 represents an invalid, inaccessible space.

        # You may ADD parameters/attributes/methods to this class as you see fit.
        # BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES IN THIS CLASS

        # The map MUST be stored in a nested list as described in the load_map() function's docstring below
        self.map = self.load_map(map_data)
        self.location = self.load_location(location_data)
        self.items = self.load_items(items_data)
        # NOTE: You may choose how to store location and item data; create your own World methods to handle these
        # accordingly. The only requirements:
        # 1. Make sure the Location class is used to represent each location.
        # 2. Make sure the Item class is used to represent each item.

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def load_map(self, map_data: TextIO) -> list[list[int]]:
        """
        Store map from open file map_data as the map attribute of this object, as a nested list of integers like so:

        If map_data is a file containing the following text:
            1 2 5
            3 -1 4
        then load_map should assign this World object's map to be [[1, 2, 5], [3, -1, 4]].

        Return this list representation of the map.
        """

        lst = []
        for line in map_data:
            s = [int(i) for i in line.split()]
            lst.append(s)
        return lst

    def load_location(self, location_data: TextIO) -> dict[int: Location]:
        """
        Stores location from open file location_data as the location attribute of this object, as a dictionary where
        the key is the location number and the value is the Location itsef.
        """
        dictionary = {}
        s = location_data.read()
        lst1 = s.split("LOCATION ")
        lst1 = [i for i in lst1 if i]
        for item in lst1:
            lst2 = item.split("\n")
            lst2 = [j for j in lst2 if j]
            lst2.pop()
            num = int(lst2[0])
            coordinates = ast.literal_eval(lst2[1])
            points = int(lst2[2])
            brief_description = lst2[3]
            long_description = lst2[4]
            items_available = ast.literal_eval(lst2[5])
            directions_available = ast.literal_eval(lst2[6])
            new_location = Location(num, coordinates, points, long_description, brief_description, items_available,
                                    directions_available)
            dictionary[num] = new_location

        return dictionary

    def load_items(self, items_data: TextIO) -> dict[str: Item]:
        """
         Stores items from open file items_data as the items attribute of this object, as a dictionary with key being
         name of the item and the value being the instance of the Item class.
        """

        s = items_data.read()
        lst = s.split("\n")
        new_dict = {}
        for item in lst:
            lst_item = item.split()
            name = lst_item[5]
            world_start = lst_item[1]
            world_end = lst_item[2]
            start_pos = int(lst_item[0])
            target_pos = int(lst_item[3])
            points = int(lst_item[4])
            new_item = Item(name, start_pos, world_start, world_end, target_pos, points)
            new_dict[name] = new_item

        return new_dict

    # TODO: Add methods for loading location data and item data (see note above).

    # NOTE: The method below is REQUIRED. Complete it exactly as specified.
    def get_location(self, x: int, y: int) -> Optional[Location]:
        """Return Location object associated with the coordinates (x, y) in the world map, if a valid location exists at
         that position. Otherwise, return None. (Remember, locations represented by the number -1 on the map should
         return None.)
        """
        if self.map[y][x] != -1:
            return self.location[self.map[y][x]]

        else:
            return None



