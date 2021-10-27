from Hero import Hero
import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        hero_is_found = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                hero_is_found = True
        if not hero_is_found:
            return 0

    def view_all_heroes(self):
        print(f'------- {self.name} -------')
        for hero in self.heroes:
            print(f'{hero.name}')
    
    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} K/D:{kd}')
    
    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, opponents):
        living_heroes = []
        living_opponents = []

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in opponents.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)
            hero.fight(opponent)
            if hero.is_alive():
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(hero)
