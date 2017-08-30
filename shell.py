import core, random

current_form = 0
saiyan_moves = ['[K]amehameha', '[S]enzu Bean', '[A]ttack', '[T]ransform']
human_moves = ['[C]ombo Move', '[S]enzu Bean', '[A]ttack', '[T]ransform']
saiyan_characters = [
    core.Saiyan('Goku', 20, 25, [
        'Saiyan', 'Super Saiyan', 'Super Saiyan 2', 'Super Saiyan 3', 'SSG',
        'SSGSS'
    ], current_form),
    core.Saiyan('Gohan', 15, 20,
                ['Saiyan', 'Super Saiyan', 'Super Saiyan 2',
                 'Ultimate'], current_form),
    core.Saiyan('Vegeta', 20, 25, [
        'Saiyan', 'Super Saiyan', 'Super Vegita', 'Super Vegita 2', 'SSG',
        'SSGSS'
    ], current_form),
    core.Saiyan('Goten', 10, 15, ['Saiyan', 'Super Saiyan'], current_form),
    core.Saiyan('Trunks', 10, 15, ['Saiyan', 'Super Saiyan'], current_form),
    core.Saiyan('Future Trunks', 10, 15, [
        'Saiyan', 'Super Saiyan', 'Super Saiyan 2', 'Super Saiyan Rage'
    ], current_form)
]
characters = {
    'Saiyan': saiyan_characters,
    'Human': [],
    'Fairy Tail': [],
    'One Punch': []
}


def main():
    print('Welcome to Gladiators'.center(100))
    glad_1 = character_selection()
    glad_2 = character_selection()
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
        print(battle.take_turn())
        print(battle)
        if (glad_2.is_dead() == True):
            print('Game Over!!! {} WINS!!!'.format(glad_1.name))
            quit()
        elif (glad_1.is_dead() == True):
            print('Game Over!!! {} WINS!!!'.format(glad_2.name))
            quit()
        else:
            continue


def character_selection():
    while True:
        race_selection = input('What race do you want to be?\n-{}\n: '.format(
            '\n-'.join(key for key in characters))).title()
        if race_selection == 'Saiyan' or 'Human':
            for key in characters:
                if race_selection == 'Saiyan':
                    decision = input(
                        'Which character do you want?\n {}\n: '.format(
                            '\n'.join('Name: ' + str(c.name) +
                                      '\n Damage Low: ' + str(c.damage_low) +
                                      '\n Damage High: ' + str(c.damage_high) +
                                      '\n Tranformations: ' +
                                      str(', '.join(c.forms))
                                      for c in characters['Saiyan']))).title()
                    if decision == 'Goku':
                        fighter = characters['Saiyan'][0]
                    elif decision == 'Gohan':
                        fighter = characters['Saiyan'][1]
                    elif decision == 'Vegeta':
                        fighter = characters['Saiyan'][2]
                    elif decision == 'Goten':
                        fighter = characters['Saiyan'][3]
                elif race_selection == 'Human':
                    name = input('What is your name?').title()
                    damage_low, damage_high = core.find_damages()
                    fighter = core.Human(name, damage_low, damage_high, [
                        '', 'Kioken', 'Kioken X2', 'Kioken X3', 'Kioken X20',
                        'Kioken X100'
                    ], current_form)
                return fighter
        else:
            print('Invalid Choice... Please Try again')


if __name__ == '__main__':
    main()