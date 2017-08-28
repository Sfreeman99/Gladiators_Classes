import core, random

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
while (glad_1.is_dead() != True) or (glad_2.is_dead() != True):
    while True:
        decision = input('{}:\n what would you like to do?\n [A]ttack\n: '.
                         format(glad_1.name)).upper()
        if decision == 'A':
            core.Moves.normal_attack(glad_1, glad_2)
            break
        else:
            print('Invalid Choice... Please try again\n')
    print(core.Battle.__str__(glad_1, glad_2))
    if (glad_2.is_dead() == True):
        print('Game Over!!! {} WINS!!!'.format(glad_1.name))
        quit()
    while True:
        decision = input('{}:\n what would you like to do?\n [A]ttack\n: '.
                         format(glad_2.name)).upper()
        if decision == 'A':
            core.Moves.normal_attack(glad_2, glad_1)
            break
        else:
            print('Invalid Choice... Please try again\n')

    print(core.Battle.__str__(glad_1, glad_2))
    if (glad_2.is_dead() == True):
        print('Game Over!!! {} WINS!!!'.format(glad_2.name))
        quit()