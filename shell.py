import core, random


def turn(attacker, defender):
    while True:
        decision = input(
            '{}:\n what would you like to do?\n [A]ttack\n[H]eal\n: '.format(
                attacker.name)).upper()
        if decision == 'A':
            attacks = core.Moves.normal_attack(attacker, defender)
            message = '{} hit {} with a {} point hit'.format(
                attacker.name, defender.name, attacks)
            return message
        if decision == 'H':
            heal = core.Moves.heal(attacker)
            message = '{} healed {} points of health'.format(
                attacker.name, heal)
            return message
        else:
            print('Invalid Choice... Please try again\n')


print('Welcome to Gladiators'.center(100))
name = input('What is Gladiator One\'s Name? \n: ').title()
health = 100
rage = 0
damage_low, damage_high = core.find_damages()
glad_1 = core.Fighter(name, health, rage, damage_low, damage_high)
name = input('What is Gladiator Two\'s Name? \n: ').title()
damage_low, damage_high = core.find_damages()
glad_2 = core.Fighter(name, health, rage, damage_low, damage_high)
print(
    "{} has a damage low of {} and damage high of {}\n {} has a damage low of {} and a damage high of {}".
    format(glad_1.name, glad_1.damage_low, glad_1.damage_high, glad_2.name,
           glad_2.damage_low, glad_2.damage_high))
print('Ready'.center(100))
print('Fight!!!'.center(100))
print(core.Battle.__str__(glad_1, glad_2))
decision = ''
while True:
    print(turn(glad_1, glad_2))
    print(core.Battle.__str__(glad_1, glad_2))
    if (glad_2.is_dead() == True):
        print('Game Over!!! {} WINS!!!'.format(glad_1.name))
        quit()
    print(turn(glad_2, glad_1))
    print(core.Battle.__str__(glad_1, glad_2))
    if (glad_1.is_dead() == True):
        print('Game Over!!! {} WINS!!!'.format(glad_2.name))
        quit()