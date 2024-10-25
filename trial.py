"""
Trial tests
"""

from typing import Optional, TextIO
import ast

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
    position: tuple
    full_description: str
    breif_description: str
    available_items: list[str]
    visited: bool
    possible_movements: list[str]

    def __init__(self, num: int, position: tuple, full_description: str, brief_description: str, available_items: list[str], possible_movements: list[str]) -> None:
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
        self.full_description = full_description
        self.breif_description = brief_description
        self.available_items = available_items
        self.visited = False
        self.possible_movements = possible_movements

def load_items(items_data: TextIO) -> dict[str: Item]:
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


def load_location(location_data: TextIO) -> dict[int: Location]:
    """
    Stores location from open file location_data as the location attribute of this object, as a dictionary where
    the key is the location number and the value is the Location itsef.
    """
    dict = {}
    s = location_data.read()
    lst1 = s.split("LOCATION ")
    lst1 = [i for i in lst1 if i]
    for item in lst1:
        lst2 = item.split("\n")
        lst2 = [j for j in lst2 if j]
        lst2.pop()
        num = int(lst2[0])
        coordinates = ast.literal_eval(lst2[1])
        brief_description = lst2[3]
        long_description = lst2[4]
        items_available = ast.literal_eval(lst2[5])
        directions_available = ast.literal_eval(lst2[6])
        new_location = Location(num, coordinates, brief_description, long_description, items_available,
                                directions_available)
        dict[num] = new_location

    return dict
