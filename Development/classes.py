class Mario :

    _lives = 3
    _speed = 30.00

    def test(self):
        print("Your stats:")
        print("lives: ", self._lives, " ", "speed: ", self._speed)

instanceMario = Mario()

print(instanceMario._speed)
instanceMario.test()
