from os import fsdecode
import random
from Ability import Ability
from Armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
    
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print(f'{self.name} and {opponent.name} draw')
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                if len(self.abilities) > 0:
                    total_damage = self.attack()
                    if len(opponent.armors) > 0:
                        total_damage -= opponent.block()
                    opponent.take_damage(total_damage)
                if len(opponent.abilities) > 0:
                    total_damage = opponent.attack()
                    if len(self.armors) > 0:
                        total_damage -= self.block()
                    self.take_damage(total_damage)
            if self.is_alive():
                print(f'{self.name} Wins')
            else:
                print(f'{opponent.name} Wins')
                

    def add_ability(self, ability):
        self.abilities.append(ability)

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

if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)