"""Functions for implementing the rules of the classic arcade game Pac-Man."""


# Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
# :param power_pellet_active: bool - does the player have an active power pellet?
# :param touching_ghost: bool - is the player touching a ghost?
def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

# The function should return True if Pac-Man is touching a power pellet or a dot.
def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


#Trigger the victory event when all dots have been eaten. Define the lose() function that takes two parameters
# param power_pellet_active: if Pac-Man has a power pellet active
# param touching_ghost: if Pac-Man is touching a ghost
#returns: Boolean value if Pac-Man wins
def lose(power_pellet_active, touching_ghost):
    return touching_ghost and not power_pellet_active

# Trigger the victory event when all dots have been eaten. Define the win() function that takes three parameters
# param has_eaten_all_dots: if Pac-Man has eaten all of the dots
# param power_pellet_active: if Pac-Man has a power pellet active
# param touching_ghost: if Pac-Man is touching a ghost
# returns: Boolean value if Pac-Man wins
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost) 
