

class Generation:
    def __init__(self, random, unit, generation_mutation_chance, unit_size):
        self.random = random
        self.unit = unit
        self.generation_mutation_chance = generation_mutation_chance
        self.unit_size = unit_size
        self.units = []

    def __str__(self):
        return 'Generation: [random: {}, unit: {}, generation_mutation_chance (). unit_size {}, units: [size: {}]]'.format(self.random, self.unit, self.generation_mutation_chance, self.unit_size, '...')

    def create_generation(self):
        generation = Generation(self.random, self.unit, self.generation_mutation_chance, self.unit_size)
        generation.units = [self.unit.create_unit() for x in range(self.unit_size)]

        generation.calculate_scores()

        return generation

    def create_multiplication(self):
        generation = Generation(self.random, self.unit,  self.generation_mutation_chance, self.unit_size)

        for x in range(self.unit_size):
            parent_first = self.units[self.random.rand() - 1]
            parent_second = self.units[self.random.rand() - 1]
            cross_index = self.random.rand()

            mutation = False
            if self.generation_mutation_chance > self.random.rand():
                mutation = True

            generation.units.append(self.unit.create_child(parent_first, parent_second, cross_index, mutation))

            generation.calculate_scores()

        return generation

    def elimination(self, generation_first, generation_second):
        generation = Generation(self.random, self.unit, self.generation_mutation_chance,  self.unit_size)

        for x in range(self.unit_size):
            unit_first = generation_first.units[x]
            unit_second = generation_second.units[x]
            if unit_first.score < unit_second.score:
                generation.units.append(unit_first)
            else:
                generation.units.append(unit_second)

        return generation

    def calculate_scores(self):
        for unit in self.units:
            unit.calculate_score()
