"""Aliens have invaded a space ship and our hero has 
to go through a maze of rooms defeating them so he 
can escape into an escape pod to the planet below. The 
game will be more like a Zork or Adventure type game 
with text outputs and funny ways to die. The game will 
involve an engine that runs a map full of rooms or scenes. 
Each room will print its own description when the player 
enters it and then tell the engine what room to run next out 
of the map."""

### SCENES ###
# DEATH - when player dies
# CENTRAL CORRIDOR - Starting point with Gothon and joke
# LASER WEAPON ARMORY - Where hero gets bomb
# THE BRIDGE - Battle scene where hero places the bomb
# ESCAPE POD - Where hero escapes after guessing the right one

### CLASSES ###
# Alien
# Player
# Gothon 
# Ship
# Planet 
# Map 
    # - next scene
    # - opening scene
# Scene 
    # - enter / description
    # Death 
    # Central Corridor 
    # Laser Weapon Armory 
    # The Bridge 
    # Escape Pod 
# Engine 
    # - play

class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(slef, scene_map):
        pass


class Death(Scene):

    def enter(self):
        pass


class CentralCorridor(Scene):

    def enter(self):
        pass


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass 


class EscapePod(Scene):

    def enter(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
