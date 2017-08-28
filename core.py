import random


def find_damages():
    ''' None -> int, int

    returns two random integars

    '''
    damage_low = random.randint(1, 10)
    damage_high = random.randint(10, 20)
    return damage_low, damage_high


class Fighter:
    ''' Initiation of parameters that will fit with all available fighters'''

    def __init__(self, name, health, rage, damage_low, damage_high, moves,
                 forms):
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.name = name
        self.moves = moves
        self.forms = forms

    def is_dead(self):
        ''' (Fighter) -> Bool

        Return True if the fighter health is 0 or below

        '''
        if self.health <= 0:
            return True
        return False

    def __repr__(self):
        ''' (Fighter) -> str

        String Representation of the following:
            Fighter((Name), (Health), (Rage), (damage_low), (damage_high))
        '''
        return "Fighter('{}', {}, {}, {}, {}, [{}])".format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high, ', '.join(map(str, self.moves)))

    def __str__(self):
        ''' (Fighter) -> str

        String Representation of the following:
            (Name) || (health) hp || (Rage) Rage!! || Low Damage: (Damage_low) || High Damage: (Damage_high)
        '''
        return "{} || {} hp || {} Rage!! || Low Damage: {} || High Damage: {}\nMoves: {}".format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high, ', '.join(map(str, self.moves)))


class Saiyan(Fighter):
    ''' Fighters based off of Dragonball Z '''

    def __init__(self, damage_low, damage_high):
        super().__init__(name, health, rage, damage_low, damage_high)
        self.damage_low = random.randint(15, 20)
        self.damage_high = 25
        self.current_form = 0

    FORM_NAMES = [
        'Saiyan', 'Super Saiyan', 'Super Saiyan 2', 'Super Saiyan 3', 'SSG',
        'SSGSS'
    ]

    def transform(self):
        message = 'You Do Not Have Enough Rage!'
        if self.rage < 80:
            return 'You Do Not Have Enough Rage!'
        elif self.current_form >= len(Saiyan.FORM_NAMES) - 1:
            return 'Max Power!!! No More Forms'
        else:
            self.health += 10
            self.damage_high += 10
            self.damage_low += 10
            self.rage = 20
            self.current_form += 1
            message = 'You Transformed To A {}'.format(
                Saiyan.FORM_NAMES[self.current_form])
            return message
        return message

    def __str__(self):
        ''' (Saiyan) -> str

        String Representation of the following:
            (Curent Form) (Name) || (health) hp || (Rage) Rage!!
        
        '''
        return "{} {} || {} hp || {} Rage!!".format(
            self.FORM_NAMES[self.current_form], self.name, self.health,
            self.rage)


class Move:
    ''' a bunch of set moves '''

    def normal_attack(self, other):
        ''' (Fighter, Fighter) -> Numbers

        Fighter attacks another Fighter to lower their health

        >>> Moves.normal_attack(Fighter('Blah', 100, 0, 15, 15),(Fighter('dook', 100, 0, 15, 15)))
        (15, 85, 15)
        '''
        attacks = random.randint(self.damage_low, self.damage_high)
        if random.randint(1, 100) <= self.rage:
            other.health -= 2 * attacks
            self.rage = 0
            message = '{} hit {} with a Critical Hit of {} damage'.format(
                self.name, other.name, attacks)
        else:
            other.health -= attacks
            self.rage += 15
            message = '{} hit {} for {} damage'.format(self.name, other.name,
                                                       attacks)
        return attacks

    def heal(self):
        ''' (Moves) -> int

        Gives the fighter 5 health

        '''
        heal = 5
        if self.rage >= 15:
            self.rage -= 15
            self.health += heal
            return heal
        else:
            return None

    def kamehameha(self, other):
        ''' (Move, Fighter) -> int

        Returns the damage of a kamehameha and if lucky you may do a super kamehameha which
        is two times the damage of a regular kamehameha

        '''
        if self.rage >= 30:
            if random.randint(1, 100) <= self.rage:
                attack = 30 * 2
                other.health -= attack
                self.rage -= 30

            else:
                attack = 30
                other.health -= attack
                self.rage -= 30
            return attack

    def saiyan_transformation(self):
        ''' (Saiyan) -> New Form
        
        Returns a new form if you meet the rage requirements
        
        '''
        message = 'You Do Not Have Enough Rage!'
        if self.rage < 80:
            return 'You Do Not Have Enough Rage!'
        elif self.current_form >= len(Saiyan.FORM_NAMES) - 1:
            return 'Max Power!!! No More Forms'
        else:
            self.health += 10
            self.damage_high += 10
            self.damage_low += 10
            self.rage = 20
            self.current_form += 1
            message = 'You Transformed To A {}'.format(
                Saiyan.FORM_NAMES[self.current_form])
            return message
        return message


class Battle:
    ''' Shows the current stats of both fighters '''

    def __init__(self, fighter_1, fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.is_f1_turn = True

    def take_turn(self):
        ''' '''
        if self.is_f1_turn:
            attacker = self.fighter_1
            defender = self.fighter_2
            self.is_f1_turn = False
        else:
            attacker = self.fighter_2
            defender = self.fighter_1
            self.is_f1_turn = True
        while True:
            decision = input(
                '{}:\n what would you like to do?\n [A]ttack\n[H]eal\n: '.
                format(attacker.name)).upper()
            if decision == 'A':
                attacks = Move.normal_attack(attacker, defender)
                message = '{} hit {} with a {} point hit'.format(
                    attacker.name, defender.name, attacks)
                return message
            if decision == 'H':
                heal = Move.heal(attacker)
                message = '{} healed {} points of health'.format(
                    attacker.name, heal)
                return message
            else:
                print('Invalid Choice... Please try again\n')

    def __str__(self):
        ''' (Battle, Battle) -> str

        String Representation of the following:
            (Name) || (health) hp || (Rage) Rage!! ||| (Name) hp || (health) hp || (Rage) Rage!!

        '''
        return "{} ||| {}\n".format(str(self.fighter_1), str(self.fighter_2))
