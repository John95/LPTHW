print '' # Exercise 35: Branches and Functions

from random import shuffle
import os

class world(object):
    turn_counter = 0
    brute_force_failed = False

def d10():
    roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle(roll)
    return roll[0]

def agility_check():
    agility = d10()
#    print agility
    return agility

def strength_check():
    strength = d10()
#    print strength
    return strength

def endurance_check():
    endurance = d10()
#    print endurance
    return endurance

def brute_force(check_against):
    if check_against <= strength_check():
#        print 'success'
        return True
    elif check_against > strength_check():
#        print 'failure'
        return False

def main():
    game_world = world()
    where_to_next = intro
    while True:
        where_to_next = where_to_next(game_world)
        game_world.turn_counter += 1

def intro(game_world):
    print "You awaken. Looking around, you find you are in a strange room.\n"
    print """  Your head hurts. 'what happened?..' You're in a small room that
looks like it hasn't been used in months. Cob-webs appear to shift
in the dimly lit room.\n"""
    print """  Your head hurts. You reach to the left side of your head and
notice that it feels bruised. You have a headache.\n"""
    print """  You sit up. You feel groggy. You remember something through the
fog of your concussion. You were on your way to work one morning when you
were abducted! What were you doing in a research facility that warranted
a kidnapping!?\n"""
    print """  Coming to from your inner dialogue, you hear a disturbance
outside your room door. Someone is coming.\n"""
    print """  Not knowing the intent of your intruder, you search frantically
for an escape. You look left and right. You see a fire escape.
Fighting back an intense headache, you lurch forward and reach for the fire
escape. The intruder enters your room. It seems like time has stopped.\n"""
    raw_input("\n--press any key to continue--\n")
    return first_encounter

def first_encounter(game_world):
    if game_world.turn_counter >= 5:
        print "Your opponent was stuck in time so long that he just disappeared! Congratulations!"
        win(game_world)
    next = raw_input("What do you do?\n-=> ").lower()
    if next == 'open fire escape' and game_world.brute_force_failed:
        print "You cannot attempt this again."
        return first_encounter
    elif next == 'open fire escape'and not game_world.brute_force_failed:
        return open_fire_escape(game_world)
    else:
        print "I don't understand."
        return first_encounter
   
def open_fire_escape(game_world):
    print "The fire escape door seems to be blocked by a wedge or something."
    next2 = raw_input("Would you like to try to brute force it?\n-=> ").lower()
    if next2 == 'yes':
        game_world.brute_force_failed = not brute_force(4)
        if game_world.brute_force_failed:
            print "You failed your attempt to brute force the door"
            return first_encounter
        print "You run out the fire escape to freedom!"
        win(game_world)
    else:
        return first_encounter
    
def win(game_world):
    print "you win!"
    print game_world.turn_counter
    exit()

main()

'''from sys import exit

def gold_room():
    print "This room is full of gold. How many doubloons do you take?"
    next = int(raw_input('> '))

    if next < 0:
        print "Wow! You're so generous, you win!"
        exit(0)
    elif next < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == 'take honey':
            dead("The bear looks at you then slaps your face off.")
        elif next == 'taunt bear' and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == 'taunt bear' and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == 'open door' and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for you life or eat your head?"

    next = raw_input("> ")

    if 'flee' in next:
        start()
    elif 'head' in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    restart()

def restart():
    choice = raw_input("\nWould you like to 'restart', or 'quit'? > ").lower()

    if 'r' in choice:
        start()
    elif 'q' in choice:
        exit(0)
    else:
        print "\nHint: type 'restart' or 'quit'"
        restart()

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if 'left' in next:
        bear_room()
    elif 'right' in next:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()'''