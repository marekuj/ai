

class Generation:
    def __init__(self, random, specimen, mutation_count, specimen_size):
        self.random = random
        self.specimen = specimen
        self.mutation_count = mutation_count
        self.specimen_size = specimen_size
        self.specimens = []

    def __str__(self):
        return 'Generation: [random: {}, specimen: {}, mutation_count {}, specimen_size {}, specimens: [size: {}]]'.format(self.random, self.specimen, self.mutation_count, self.specimen_size, '...')

    def create_generation(self):
        generation = Generation(self.random, self.specimen, self.mutation_count, self.specimen_size)
        generation.specimens = [self.specimen.create_specimen() for x in range(self.specimen_size)]

        generation.calculate_scores()

        return generation

    def create_multiplication(self):
        generation = Generation(self.random, self.specimen,  self.mutation_count, self.specimen_size)

        for x in range(self.specimen_size):
            parent_first = self.specimens[self.random.rand()]
            parent_second = self.specimens[self.random.rand()]
            generation.specimens.append(self.specimen.create_child(parent_first, parent_second))

        generation.make_mutation()
        generation.calculate_scores()

        return generation

    def elimination(self, generation_first, generation_second):
        generation = Generation(self.random, self.specimen, self.mutation_count,  self.specimen_size)

        for x in range(self.specimen_size):
            specimen_first = generation_first.specimens[x]
            specimen_second = generation_second.specimens[x]
            if specimen_first.score < specimen_second.score:
                generation.specimens.append(specimen_first)
            else:
                generation.specimens.append(specimen_second)

        return generation

    def make_mutation(self):
        for x in range(self.mutation_count):
            self.specimens[self.random.rand()].mutation()

    def calculate_scores(self):
        for specimen in self.specimens:
            specimen.calculate_score()
