from sys import exit
from random import randint

class Scene(object):

    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))

    def enter(self):
        print "You have just entered a room"
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        #print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        #print "Play's first scence", current_scene
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew.  You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge, and blow the ship up after getting into an "
        print "escape pod."
        print "\n"
        #print "You're running down the central corridor to the Weapons Armory when"
        #print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        #print "flowing around his hate filled body.  He's blocking the door to the"
        #print "Armory and about to pull a weapon to blast you."

        while True:
        #    print "\n----------"
            next_scene_name = current_scene.enter()
        #    print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
        #    print "map returns new scene", current_scene


class Death(Scene):

    quips = [
          "You died.  You kinda suck at this.",
            "My cat's tails is better at this.",
            "It's ok, you can try again, but you'll probably still loose."]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print "You are in the central corridor."

        action = raw_input("> ")

        if action.lower() in ("look", "look around", "view"):
            print "The room is long and cylindrical with strange markings above"
            print "the doors.  To the right looks like the Weapons Armory.  To the left"
            print "there is an unmarked door."
            return 'central_corridor'

        elif action.lower() in ("unmarked", "unmarked room", "left"):
            #TODO - figure out how to say "like" in if statements above
            print "You are brave and head into the unmarked room."
            return 'unmarked_room'

        elif action.lower() in ("weapon", "weapons", "armory", "weapon armory", 
                        "weapons armory", "right"):
            print "You grab hold of the cold knob of the weapon armory door "
            print "and head in."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'


class UnmarkedRoom(Scene):

    def enter(self):
        print "You are inside the unmarked room and there is no light to see."

        action = raw_input("> ")

        if action in ("look", "view"):
            print "There's not much to see, but the walls have an interesting texture."
            return "unmarked_room"

        elif action in ("touch", "feel", "touch wall", "wall", "walls"):
            print "The walls in this room are made of an interesting brick."
            print "They are slimy and jagged.  Staying close to the wall you notice"
            print "a loose brick."
            return 'unmarked_room'

        elif action in ("brick", "move brick"):
            print "You remove a loose, slimy brick from the wall.  Three cards fall out"
            print "with dots on them.  One has %s dots, the next %s dots, and the last" % (self.code[2], self.code[0])
            print "%s dots.  You take note and put them back so a Gothon doesn't" % self.code[1]
            print "find out you've been here."
            return 'unmarked_room'

        elif action in ("go back", "back", "central corridor", "central"):
            print "You decide to head back to the central corridor where you can see."
            return 'central_corridor'

        else:
            print "DOES NOT COMPUTE!"
            return 'unmarked_room'
        

class LaserWeaponArmory(Scene):

    def enter(self):
        print "Inside the Weapon Armory you notice a container across the room."
        print "The label suggests this is the neutron bomb.  There's a keypad lock on the box"
        print "and you need the code to get the bomb out.  Only 10 guesses are"
        print "permitted at a time.  There are only 3 spots to fill with a digit."
        #code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != self.code and guesses < 9:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == self.code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'

        else:
            print "The lock buzzes one last time and the keypad no longer registers your touch."

            action = raw_input("> ")

            if action in ("go back", "central corridor", "leave", "look", "back"):
                print "Maybe the code is lying around somewhere.  You try"
                print "heading back to the central corridor."
                return 'central_corridor'

            else:
                print "You don't know what to do next, so you curl into a ball"
                print "and wait for the Gothons to blow up the ship."
                return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst onto the Bridge with the netron destruct bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship.  Each of them has an even uglier"
        print "clown costume than the last.  They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."

        action = raw_input("> ")

        if action in ("throw the bomb", "bomb", "throw"):
            print "In a panic you throw the bomb at the group of Gothons"
            print "and make a leap for the door.  Right as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'

        elif action in ("slowly place the bomb", "place bomb", "place"):
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jump back through the door, punch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can."
            return 'escape_pod'

        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge" 


class EscapePod(Scene):

    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the escape pod before the whole ship explodes.  It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference.  You get to the chamber with the escape pods, and"
        print "now need to pick one to take.  Some of them could be damaged"
        print "but you don't have time to look.  There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below.  As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time.  You won!"


            return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'unmarked_room': UnmarkedRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        #print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        #print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        #print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
