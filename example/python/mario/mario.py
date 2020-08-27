from util import *


def get_position_in_direction(position, direction):
    """
    Determines the position that would result from moving the
    given position in the given direction

    If the direction "r" is given, increase the x coordinate by 1.
    If the direction "l" is given, decrease the x coordinate by 1.
    If the direction "u" is given, increase the y coordinate by 1.
    If the direction "d" is given, decrease the y coordinate by 1.

    Parameters:
        position (<int, int>): represents (x, y) coordinates
        direction (str): "r", "l", "u" or "d" representing right, left, up, and down

    Return:
        <int, int>: position relative to the given direction
    """
    x, y = position
    dx, dy = DIRECTIONS[direction]
    return x + dx, y + dy


def get_tile_at_position(level, position):
    """
    Gets the character representing the tile at the
    given position in a level string

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates

    Return:
        str: tile at given position in the level
    """
    return level[position_to_index(position, level_size(level))]


def get_tile_in_direction(level, position, direction):
    """
    Retrieves the tile in the direction relative to the given
    position from the level.

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates
        direction (str): "r", "l", "u" or "d" representing right, left, up, and down

    Return:
        str: tile at the position in the given direction
    """
    return get_tile_at_position(level, get_position_in_direction(position, direction))


def remove_from_level(level, position):
    """
    The tile at the given position in the level is replaced with an AIR tile
    and the new level string is returned

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates

    Return:
        str: updated level string
    """
    index = position_to_index(position, level_size(level))
    return level[:index] + AIR + level[index + 1:]


def move(level, position, direction):
    """
    Returns the position in the given direction

    If the tile at the new position is a wall tile the y coordinate is increased
    until an AIR tile is found at the new position

    If the tile directly below the new position is an AIR tile the y
    coordinate is decreased until tile directly below is not an AIR tile.

    It is assumed the level map has a valid position within index bounds

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates
        direction (str): "r", "l", "u" or "d" representing right, left, up, and down

    Return:
        <int, int>: updated position in direction
    """
    new_position = get_position_in_direction(position, direction)

    # Handle climbing up a hill
    next_item = get_tile_at_position(level, new_position)
    while next_item == WALL:
        new_position = (new_position[0], new_position[1] + 1)
        next_item = get_tile_at_position(level, new_position)

    # Handle falling down
    below = get_position_in_direction(new_position, DOWN)
    floor = get_tile_at_position(level, below)
    while floor == AIR:
        new_position = (new_position[0], new_position[1] - 1)
        below = get_position_in_direction(new_position, DOWN)
        floor = get_tile_at_position(level, below)

    return new_position


def print_level(level, position):
    """
    prints the level string with the given position replaced by the PLAYER
    character.

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates

    """
    index = position_to_index(position, level_size(level))
    print(level[:index] + PLAYER + level[index + 1:])


def attack(level, position):
    """
    Checks if there is a MONSTER tile to the left of the given position, if there
    is then "Attacking the monster on your left!" is printed and the level is
    returned with the tile removed.

    If no then this check is repeated for the right direction and prints
    "Attacking the monster on your right!"

    If there is no MONSTER then "No monsters to attack!" is output with the
    the level unchanged

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates

    Return:
        str: level string with MONSTER tile removed or unchanged
    """
    left_position = get_position_in_direction(position, LEFT)
    left = get_tile_at_position(level, left_position)

    right_position = get_position_in_direction(position, RIGHT)
    right = get_tile_at_position(level, right_position)

    if left == MONSTER:
        print("Attacking the monster on your left!")
        return remove_from_level(level, left_position)
    elif right == MONSTER:
        print("Attacking the monster on your right!")
        return remove_from_level(level, right_position)
    else:
        print("No monsters to attack!")
        return level


def tile_status(level, position):
    """
    If the tile at the position is the GOAL tile then
    "Congratulations! You finished the level" is printed and returns None.

    If the tile at the position is a MONSTER tile then
    "Hit a monster! Game over!" is printed and returns None.

    If the tile at the position is a COIN or CHECKPOINT tile it is removed from
    the level

    Parameters:
        level (str): represents a 2D level map
        position (<int, int>): represents (x, y) coordinates

    Return:
        <str, str>: represents (tile, level) with tile being the tile at the
            given position in the original level and level is updated or unchanged

    """
    tile = get_tile_at_position(level, position)

    # Handle winning
    if tile == GOAL:
        print("Congratulations! You finished the level")

    # Handle monster death
    if tile == MONSTER:
        print("Hit a monster!")

    # Handle picking up coins and reaching checkpoints
    if tile in (COIN, CHECKPOINT):
        level = remove_from_level(level, position)

    return tile, level


def main():
    """
    Handles the main interaction with the user

    Prompts for a filename located at levels/{level_name} to load.
    Continues to prompt the user for an action until the goal is reached or
    game over from encountering a monster.
    """
    level = load_level("example/python/mario/level.txt")
    score = 0
    position = (0, 1)

    level_checkpoint = level
    score_checkpoint = score
    position_checkpoint = position

    while True:
        print(f"Score: {score}")
        print_level(level, position)

        command = input("Please enter an action (enter '?' for help): ")

        if command in (LEFT, RIGHT):
            position = move(level, position, command)
            tile, level = tile_status(level, position)

            if tile == GOAL:
                break
            elif tile == MONSTER:
                level = level_checkpoint
                score = score_checkpoint
                position = position_checkpoint
            elif tile == COIN:
                score += 1
            elif tile == CHECKPOINT:
                level_checkpoint = level
                score_checkpoint = score
                position_checkpoint = position

        if command == 'a':
            level = attack(level, position)

        if command == '?':
            print(HELP_TEXT)

        if command == 'n':
            position = position_checkpoint
            score = score_checkpoint
            level = level_checkpoint

        if command == 'q':
            break


if __name__ == "__main__":
    main()
