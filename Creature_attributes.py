class Player_character:
    def __init__(self, ability_scores,
                 name,
                 player_class,
                 health_points,
                 attack,
                 defense):
        self.ability_scores = ability_scores
        self.name = name
        self.player_class = player_class
        self.health_points = health_points
        self.attack = attack
        self.defense = defense
        
    def update_scores(self):
        print(f'''Ability Scores:
            STR: {self.ability_scores[0]}
            DEX: {self.ability_scores[1]}
            CON: {self.ability_scores[2]}
            INT: {self.ability_scores[3]}
            WIS: {self.ability_scores[4]}
            CHA: {self.ability_scores[5]}''')
        update = input("Update ability score? Y/N ")
        if update == "Y":
            select_score = input('''Which score should be updated?
                                STR/DEX/CON/INT/WIS/CHA''')
            if select_score == 'STR':
                STR = input('Enter score ')
                self.ability_scores[0] = int(STR)
            elif select_score == 'DEX':
                DEX = input('Enter score ')
                self.ability_scores[1] = int(DEX)
            elif select_score == 'CON':
                CON = input('Enter score ')
                self.ability_scores[2] = int(CON)
            elif select_score == 'INT':
                INT = input('Enter score ')
                self.ability_scores[3] = int(INT)
            elif select_score == 'WIS':
                WIS = input('Enter score ')
                self.ability_scores[4] = int(WIS)
            elif select_score == 'CHA':
                CHA = input('Enter score ')
                self.ability_scores[5] = int(CHA)
        else:
            pass
        return self.ability_scores
    
    def Character_name(self):
        print("Greetings, mighty " + self.name +"!")

    def Character_attack(self):
        import random
        result = int(random.randrange(1,20) + self.attack)
        print(self.name + " attacks!")
        print(result)
        return result
    
    def Character_defense(self, result, weapon_damage):
        if result >= self.defense:
            print(self.name + " is hit!")
        else:
            print("Attack misses!")

class Weapon:
    def __init__(self, name, damage_type, attack_bonus, max_damage, bonus_damage, bonus_damage_type):
        self.name = name
        self.damage_type = damage_type
        self.attack_bonus = attack_bonus
        self.max_damage = max_damage
        self.bonus_damage = bonus_damage
        self.bonus_damage_type = bonus_damage_type

    def Weapon_damage(self):
        import random
        damage = int(random.randrange(1,self.max_damage))
        return damage

class Monster:
    def __init__(self, name, monster_type, health_points, attack, defense):
        self.name               = name
        self.monster_type       = monster_type
        self.health_points      = health_points
        self.attack             = attack
        self.defense            = defense
    
    def Monster_attack(self):
        import random
        result = int(random.randrange(1,20) + self.attack)
        print(self.name + " attacks!")
        print(result)
        return result

    def Monster_defense(self, result, weapon_damage):
        if result >= self.defense:
            print(self.name + " is hit!")
        else:
            print("Attack misses!")
