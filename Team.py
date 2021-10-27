from Hero import Hero

class Team:
    def __init__ (self, name):
        self.name = name
        self.heroes = []

    def remove_hero (self, name):
        hero_is_found = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                hero_is_found = True
        if not hero_is_found:
            return 0

    def view_team (self):
        print(f'------- {self.name} -------')
        for hero in self.heroes:
            print(f'{hero.name}')
    
    def add_hero (self, hero):
        self.heroes.append(hero)

    