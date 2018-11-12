from collections import OrderedDict
from operator import itemgetter


class Unit:
    def __init__(self, random, travel_cost_table, genes_size):
        self.random = random
        self.travel_cost_table = travel_cost_table
        self.genes_size = genes_size
        self.score = -1
        self.genes = []

    def __str__(self):
        return 'Unit: [random: {}, score {}, genes_size {}, genes: {}]'.format(self.random, self.score, self.genes_size, self.genes)

    def create_unit(self):
        unit = Unit(self.random, self.travel_cost_table, self.genes_size)
        unit.genes = [self.random.rand() for x in range(self.genes_size)]
        return unit

    def create_child(self, parent_first, parent_second, cross_index, mutation):
        child = Unit(self.random, self.travel_cost_table, self.genes_size)
        child.genes = parent_first.genes[:cross_index] + parent_second.genes[cross_index:]
        if mutation:
            child.genes[self.random.rand() & self.genes_size - 1] = self.random.rand()

        return child

    def get_route(self):
        route = {}
        for idx, value in enumerate(self.genes):
            route[idx] = value

        return list(OrderedDict(sorted(route.items(), key=itemgetter(1), reverse=True)).keys())

    def calculate_score(self):
        route = self.get_route()
        self.score = sum([self.travel_cost_table.costs[route[x]][route[x + 1]] for x in range(self.genes_size - 1)])

        return self.score
