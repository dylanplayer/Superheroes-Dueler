from Ability import Ability
from Weapon import Weapon
from Armor import Armor
from Hero import Hero
from Team import Team

class Arena:
    def __init__(self):
        self.team_one = Team('Team 1')
        self.team_two = Team('Team 2')
    
    def create_ability(self):
        name = input('What is the ability name? ')
        max_damage = int(input('What is the max damage of the ability? '))
        return Ability(name, max_damage)

    def create_weapon(self):
        name = input('What is the name of the weapon? ')
        max_damage = int(input('What is the max damage of the weapon? '))
        return Weapon(name, max_damage)
    
    def create_armor(self):
        name = input('What is the name of the armor? ')
        max_defense = int(input('What is the max defense of the armor? '))
        return Armor(name, max_defense)
    
    def create_hero(self):
        hero_name = input('Hero\'s name? ')
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                hero.add_ability(self.create_ability())
            elif add_item == "2":
                hero.add_weapon(self.create_weapon())
            elif add_item == "3":
                hero.add_armor(self.create_armor())
        return hero

    def build_team_one(self):
        number_of_heros = int(input('Number of heroes? '))
        for i in range(number_of_heros):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        number_of_heros = int(input('Number of heroes? '))
        for i in range(number_of_heros):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_team_stats(self, team):
        print('--------------------------')
        team_kills = 0
        team_deaths = 0
        print(f'\n{team.name} stats: \n{team.stats()}\n')
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f'{team.name} average K/D was: {str(team_kills/team_deaths)}')
        print('Survivors: ')
        for hero in team.heroes:
            if hero.deaths == 0:
                print(hero.name)

    
    def show_stats(self):
        self.show_team_stats(self.team_one)
        self.show_team_stats(self.team_two)

if __name__ == "__main__":
    game_is_running = True
    arena = Arena()

    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        if play_again.lower() == "n":
            game_is_running = False
        else:
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()