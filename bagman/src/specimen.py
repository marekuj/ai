from collections import OrderedDict
from operator import itemgetter


class Specimen:
    def __init__(self, random, travel_cost_table, genes_size):
        self.random = random
        self.travel_cost_table = travel_cost_table
        self.genes_size = genes_size
        self.score = -1
        self.genes = []

    def __str__(self):
        return 'Specimen: [random: {}, score {}, genes_size {}, genes: {}]'.format(self.random, self.score, self.genes_size, self.genes)

    def create_specimen(self):
        specimen = Specimen(self.random, self.travel_cost_table, self.genes_size)
        specimen.genes = [self.random.rand() for x in range(self.genes_size)]

        return specimen

    def create_child(self, parent_first, parent_second):
        cross_index = self.random.rand_range(0, self.genes_size - 1)
        child = Specimen(self.random, self.travel_cost_table, self.genes_size)
        child.genes = parent_first.genes[:cross_index] + parent_second.genes[cross_index:]

        return child

    def mutation(self):
        mutation_index = self.random.rand_range(0, self.genes_size - 1)
        self.genes[mutation_index] = self.random.rand()

    def get_route(self):
        route = {}
        for idx, value in enumerate(self.genes):
            route[idx] = value

        return list(OrderedDict(sorted(route.items(), key=itemgetter(1), reverse=True)).keys())

    def calculate_score(self):
        route = self.get_route()
        self.score = sum([self.travel_cost_table.costs[route[x]][route[x + 1]] for x in range(self.genes_size - 1)])

        return self.score
