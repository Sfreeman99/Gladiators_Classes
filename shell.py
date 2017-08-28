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
print(glad_1)
print(glad_2)