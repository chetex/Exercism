"""Functions for implementing the rules of the classic arcade game Pac-Man."""


# Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
# :param power_pellet_active: bool - does the player have an active power pellet?
# :param touching_ghost: bool - is the player touching a ghost?
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost;

# The function should return True if Pac-Man is touching a power pellet or a dot.
def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot;


def lose(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost;


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """

    pass
