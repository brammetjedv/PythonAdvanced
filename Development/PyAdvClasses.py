class enemy:
    def __init__(self, lives, strength):
        self.lives = lives
        self.strength = strength

e1 = enemy(6, 4)



class player:
    def __init__(self, lives, strength):
        self.lives = lives
        self.strength = strength
    
    def getHurt(self):
        self.lives = self.lives - e1.strength

    def drinkHeal(self):
        self.lives = self.lives + 5


p1 = player(10, 5)
print(p1.lives)
print(p1.strength)

p1.getHurt()
print(p1.lives)

p1.drinkHeal()
print(p1.lives)