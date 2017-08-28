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

    def __init__(self, name, health, rage, damage_low, damage_high):
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.name = name

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
        return "Fighter('{}', {}, {}, {}, {})".format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __str__(self):
        ''' (Fighter) -> str

        String Representation of the following:
            (Name) || (health) hp || (Rage) Rage!! || Low Damage: (Damage_low) || High Damage: (Damage_high)
        '''
        return "{} || {} hp || {} Rage!! || Low Damage: {} || High Damage: {}".format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    # def attack(self, other):
    #     ''' (Fighter, Fighter) -> Numbers

    #     Fighter attacks another Fighter to lower their health

    #     '''
    #     attacks = random.randint(self.damage_low, self.damage_high)
    #     if random.randint(1,100) <= self.rage:
    #         other.health -= 2 * attack
    #         self.rage += 15
    #         message = '{} hit {} with a Critical Hit of {} damage'.format(self.name, other.name, attacks)
    #     else:
    #         other.health -= attacks
    #         self.rage += 15
    #         message = '{} hit {} for {} damage'.format(self.name, other.name, attacks )


class Moves:
    ''' a bunch of set moves '''

    def normal_attack(self, other):
        ''' (Fighter, Fighter) -> Numbers

        Fighter attacks another Fighter to lower their health

        >>> Moves.normal_attack(Fighter('Blah', 100, 0, 15, 15),(Fighter('dook', 100, 0, 15, 15)))
        (15, 85, 15)
        '''
        attacks = random.randint(self.damage_low, self.damage_high)
        if random.randint(1, 100) <= self.rage:
            other.health -= 2 * attack
            self.rage += 15
            message = '{} hit {} with a Critical Hit of {} damage'.format(
                self.name, other.name, attacks)
        else:
            other.health -= attacks
            self.rage += 15
            message = '{} hit {} for {} damage'.format(self.name, other.name,
                                                       attacks)
        return attacks, other.health, self.rage
