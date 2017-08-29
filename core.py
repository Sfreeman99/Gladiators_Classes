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

    def __init__(self, name, health, rage, damage_low, damage_high,
                 forms, current_form):
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.name = name
        self.forms = forms
        self.current_form = current_form

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
        return " {} {} || {} hp || {} Rage!! || Low Damage: {} || High Damage: {}\nMoves: {}\n\n".format(
            self.forms[self.current_form], self.name, self.health, self.rage,
            self.damage_low, self.damage_high, ', '.join(map(str, self.moves)))


class Saiyan(Fighter):
    ''' Fighters based off of Dragonball Z '''

    def __init__(self, name, health, rage, damage_low, damage_high,
                 forms, current_form):
        super().__init__(name, health, rage, damage_low, damage_high,
                         forms, current_form)
        self.moves = ['[K]amehameha', '[S]enzu Bean', '[A]ttack', '[T]ransform']

    def get_moves(self, other):
        decision = ''
        while True:
            decision = '{}: \n Moves: {}'.format(self.name, self.moves)
            if decision == 'A':
                return Normal_Attack.saiyan_attack(attacker, defender)
            elif decision == 'H':
                return Heal.senzu_bean()
            elif decision == 'K':
                return Special.kamehameha(attacker, defender)
            elif decision == 'T':
                return Transformation.saiyan_transformation()
            else:
                return 'Invalid Choice... Please Choose a Saiyan Move'
        def __str__(self):
            return super().__str__()


class Human(Fighter):
    ''' Information on a Human Fighter '''

    def __init__(self, name, health, rage, damage_low, damage_high,
                 forms, current_form):
        super().__init__(name, health, rage, damage_low, damage_high,
                         forms, current_form)
        self.damage_low = 5
        self.damage_high = 15
        self.moves = ['[C]ombo Move', '[S]enzu Bean', '[A]ttack', '[T]ransform']


    def get_moves(self, other):
        decision = ''
        while True:
            decision = '{}: \n Moves: {}'.format(self.name, self.moves)
            if decision == 'A':
                return Normal_Attack.human_attack(attacker, defender)
            elif decision == 'H':
                return Heal.senzu_bean()
            elif decision == 'C':
                return Special.regular_special_move(attacker, defender)
            elif decision == 'T':
                return Transformation.human_transformation()
            else:
                return 'Invalid Choice... Please Choose a Human Move'

    def __str__(self):
        return super().__str__()


class Move:
    ''' a bunch of set moves '''

    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    # def normal_attack(self, other):
    #     ''' (Fighter, Fighter) -> Numbers

    #     Fighter attacks another Fighter to lower their health

    #     >>> Moves.normal_attack(Fighter('Blah', 100, 0, 15, 15),(Fighter('dook', 100, 0, 15, 15)))
    #     (15, 85, 15)
    #     '''
    #     attacks = random.randint(self.damage_low, self.damage_high)
    #     if random.randint(1, 100) <= self.rage:
    #         other.health -= 2 * attacks
    #         self.rage = 0
    #         message = '{} hit {} with a Critical Hit of {} damage'.format(
    #             self.name, other.name, attacks)
    #     else:
    #         other.health -= attacks
    #         self.rage += 15
    #         message = '{} hit {} for {} damage'.format(self.name, other.name,
    #                                                    attacks)
    #     return attacks

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
        attacker.getmoves(attacker, defender)

    def __str__(self):
        ''' (Battle, Battle) -> str

        String Representation of the following:
            (Name) || (health) hp || (Rage) Rage!! ||| (Name) hp || (health) hp || (Rage) Rage!!

        '''
        return "{} ||| {}\n".format(str(self.fighter_1), str(self.fighter_2))


class Normal_Attack(Move):
    ''' Class full of normal attacks for different characters '''

    def __init__(self, attacker, defender):
        super().__init__(attacker, defender)

    def human_attack(self, other):
        ''' (Fighter, Fighter) -> Numbers

        Fighter attacks another Fighter to lower their health

        >>> Normal_Attack.human_attack(Fighter('Blah', 100, 0, 15, 15, [], []),(Fighter('dook', 100, 0, 15, 15, [], [])))
        15
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

    def saiyan_attack(self, other):
        ''' (Fighter, Fighter) -> Numbers

        Fighter attacks another Fighter to lower their health

        >>> Normal_Attack.saiyan_attack(Fighter('Blah', 100, 0, 15, 15, [], []),(Fighter('dook', 100, 0, 15, 15, [], [])))
        15
        '''
        attacks = random.randint(self.damage_low, self.damage_high)
        if random.randint(75, 100) <= self.rage:
            other.health -= 3 * attacks
            self.rage = 0
            message = '{} hit {} with a Critical Hit of {} damage'.format(
                self.name, other.name, attacks)
        else:
            other.health -= attacks
            self.rage += 15
            message = '{} hit {} for {} damage'.format(self.name, other.name,
                                                       attacks)
        return attacks


class Special(Move):
    ''' class full of special moves for each race '''

    def __init__(self, attacker, defender):
        super().__init__(attacker, defender)

    def regular_special_move(self, other):
        ''' (Move, Fighter) -> Int

        Returns the amount of damage the attacker did to the defender
        if the rage requirements are met

        '''
        if self.rage >= 20:
            attack = 20
            other.health -= attack
            self.rage -= 20
            message = 'Combo Move Successful'
            return attack
        else:
            return 'Not enough Rage'

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


class Transformation(Move):
    ''' class full of Transformations '''

    def __init__(self, attacker):
        super().__init__(attacker, defender)

    def human_transformation(self):
        ''' (Human) -> New Form
        
        Returns a new form if you meet the rage requirements and transformation
        Requirements
        
        '''
        message = 'You Do Not Have Enough Rage!'
        if self.rage < 80:
            return 'You Do Not Have Enough Rage!'
        elif self.current_form >= len(self.forms) - 1:
            return 'Max Power!!! No More Forms'
        else:
            self.health -= (5 * self.current_form)
            self.damage_high += 10
            self.rage = 20
            self.current_form += 1
            message = 'You Transformed To A {}'.format(
                self.forms[self.current_form])
            return message
        return message

    def saiyan_transformation(self):
        ''' (Saiyan) -> New Form

        Returns a new form if you meet the rage requirements and transformation
        Requirements
        
        '''
        message = 'You Do Not Have Enough Rage!'
        if self.rage < 80:
            return 'You Do Not Have Enough Rage!'
        elif self.current_form >= len(self.forms) - 1:
            return 'Max Power!!! No More Forms'
        else:
            self.health -= 10
            self.damage_high += (10 * self.current_form)
            self.damage_low += (10 * self.current_form)
            self.rage = 20
            self.current_form += 1
            message = 'You Transformed To A {}'.format(
                self.forms[self.current_form])
            return message
        return message


class Heal(Move):
    ''' class full of healing Moves '''

    def __init__(self, attacker, defender):
        super().__init__(attacker, defender)

    def senzu_bean(self):
        ''' (Fighter) -> int

        If rage requirement meet the user gets a certain amount of health 
        based on how their luck is at that moment. It could be your greatest
        help or backfire horribly

        '''
        bean = random.randint(1, 100)
        luck = random.randint(1, 100) + bean
        if self.rage >= 40:
            self.health += luck
            if luck > 0:
                message = 'Your Very lucky'
            else:
                message = 'You are an unlucky individual'
        return luck
