from random import randint
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(randint(1,self.sides))
die=Die(6)
for i in range(10):
    die.roll_die()
die=Die(10)
for i in range(10):
    die.roll_die()
die=Die(20)
for i in range(10):
    die.roll_die()