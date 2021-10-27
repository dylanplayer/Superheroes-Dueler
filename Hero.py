from os import fsdecode
import random
from Ability import Ability
from Armor import Armor
from Weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
        self.deaths = 0
        self.kills = 0
    
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print(f'{self.name} and {opponent.name} draw')
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                if len(self.abilities) > 0:
                    total_damage = self.attack()
                    if len(opponent.armors) > 0:
                        total_damage -= opponent.defend()
                    opponent.take_damage(total_damage)
                if len(opponent.abilities) > 0:
                    total_damage = opponent.attack()
                    if len(self.armors) > 0:
                        total_damage -= self.defend()
                    self.take_damage(total_damage)
            if self.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                print(f'{self.name} Wins')
            else:
                opponent.add_kill(1)
                self.add_death(1)
                print(f'{opponent.name} Wins')
                

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)
        
    def defend(self):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return total_armor

    def take_damage(self, damage):
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
