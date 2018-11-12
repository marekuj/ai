import random


class Random:
    def __init__(self, random_min, random_max):
        self.random_min = random_min
        self.random_max = random_max

    def __str__(self):
        return 'Random: [random_min: {}, random_max: {}]'.format(self.random_min, self.random_max)

    def rand(self):
        return random.randint(self.random_min, self.random_max)
