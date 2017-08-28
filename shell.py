import core, random


def main():
    print('Welcome to Gladiators'.center(100))
    name = input('What is Gladiator One\'s Name? \n: ').title()
    health = 100
    rage = 0
    damage_low, damage_high = core.find_damages()
    moves = ['[A]ttack', '[H]eal']
    glad_1 = core.Fighter(name, health, rage, damage_low, damage_high, moves,
                          ['Transformations'])
    name = input('What is Gladiator Two\'s Name? \n: ').title()
    damage_low, damage_high = core.find_damages()
    moves = ['[A]ttack', '[H]eal']
    glad_2 = core.Fighter(name, health, rage, damage_low, damage_high, moves,
                          ['Transformations'])
    print(
        "{} has a damage low of {} and damage high of {}\n {} has a damage low of {} and a damage high of {}".
        format(glad_1.name, glad_1.damage_low, glad_1.damage_high, glad_2.name,
               glad_2.damage_low, glad_2.damage_high))
    print('Ready'.center(100))
    print('Fight!!!'.center(100))
    battle = core.Battle(glad_1, glad_2)
    print(battle)
    decision = ''
    while True:
        battle.take_turn()
        print(battle)
        if (glad_2.is_dead() == True):
            print('Game Over!!! {} WINS!!!'.format(glad_1.name))
            quit()
        elif (glad_1.is_dead() == True):
            print('Game Over!!! {} WINS!!!'.format(glad_2.name))
            quit()
        else:
            continue


if __name__ == '__main__':
    main()