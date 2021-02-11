class Player_character:
    def __init__(self, name, player_class, health_points, attack, defense):
        self.name          = name
        self.player_class  = player_class
        self.health_points = health_points
        self.attack        = attack
        self.defense       = defense
        
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