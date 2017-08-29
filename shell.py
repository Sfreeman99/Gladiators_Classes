import core, random

health = 100
rage = 0
current_form = 0
damage_low, damage_high = core.find_damages()
saiyan_moves = ['[K]amehameha', '[S]enzu Bean', '[A]ttack', '[T]ransform']
human_moves = ['[C]ombo Move', '[S]enzu Bean', '[A]ttack', '[T]ransform']
saiyan_characters = [
        core.Saiyan('Goku', health, rage, 15, 20,[
            'Saiyan', 'Super Saiyan', 'Super Saiyan 2', 'Super Saiyan 3',
            'SSG', 'SSGSS'], current_form),
    
        core.Saiyan('Gohan',health, rage, 10, 15, [
            'Saiyan', 'Super Saiyan', 'Super Saiyan 2', 'Ultimate'
        ], current_form),
    
        core.Saiyan('Vegeta',health, rage, 15, 20, [
            'Saiyan', 'Super Saiyan', 'Super Vegita', 'Super Vegita 2', 'SSG',
            'SSGSS'
        ], current_form),
    core.Saiyan('Goten', health, rage, damage_low, damage_high, ['Saiyan', 'Super Saiyan'], current_form)]
characters = {
    'Saiyan': saiyan_characters
        
}


def main():
    print('Welcome to Gladiators'.center(100))
    name = input('What is your name\n: ').title()
    race_selection = input('What race do you want to be?\n-{}\n: '.format('\n-'.join(key for key in characters)))
    for key in characters:
        if race_selection == 'Saiyan':
            decision = input('Which character do you want?\n {}\n: '.format('\n'.join('Name: ' + str(c.name) + '\n Damage Low: ' + str(c.damage_low) + '\n Damage High: ' + str(c.damage_high) + '\n Tranformations: '  + str(', '.join(c.forms))  for c in characters['Saiyan'])))
            if decision == 'Goku':
                glad_1 = characters['Saiyan'][0]
            elif decision == 'Gohan':
                glad_1 = characters['Saiyan'][1]
            elif decision == 'Vegeta':
                glad_1 = characters['Saiyan'][2]
            elif decision == 'Goten':
                glad_1 = characters['Saiyan'][3]
        elif race_selection == 'Human':
            name = input('What is your name?').title()

    # glad_1 = core.Fighter(name, health, rage, damage_low, damage_high, moves,
    #                       ['Transformations'], current_form)
    name = input('What is Gladiator Two\'s Name? \n: ').title()
    damage_low, damage_high = core.find_damages()
    moves = ['[A]ttack', '[H]eal', '[S]pecial', '[T]ransformation']
    glad_2 = core.Fighter(name, health, rage, damage_low, damage_high, moves,
                          ['Transformations'], current_form)
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