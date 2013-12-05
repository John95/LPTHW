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
