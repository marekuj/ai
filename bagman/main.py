#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.evolve import Evolve
from src.generation import Generation
from src.random import Random
from src.travel_cost_table import TravelCostTable
from src.specimen import Specimen


def main():
    city_size = 100
    cost_random_value_min = 10
    cost_random_value_max = 60

    gene_size = city_size
    gene_random_value_min = 0
    gene_random_value_max = 255

    generation_size = 200
    generation_random_idx_min = 0
    generation_random_idx_max = generation_size - 1
    generation_mutation_count = gene_size * generation_size // 1000  # [1 mutation per 1000 genes]

    evolve_delta_stop = 250

    cost_random = Random(cost_random_value_min, cost_random_value_max)
    travel_cost_table = TravelCostTable(cost_random, city_size).create_travel_cost_table_const() # Only for table_size equals 100!
    # travel_cost_table = TravelCostTable(cost_random, city_size).create_travel_cost_table()

    print(cost_random)
    print(travel_cost_table)

    gene_random = Random(gene_random_value_min, gene_random_value_max)
    specimen = Specimen(gene_random, travel_cost_table, gene_size)
    generation_random = Random(generation_random_idx_min, generation_random_idx_max)
    generation = Generation(generation_random, specimen, generation_mutation_count, generation_size)
    evolve = Evolve(generation, evolve_delta_stop)

    print(gene_random)
    print(specimen)
    print(generation_random)
    print(generation)
    print(evolve)

    print('*' * 250)
    print('Start scores:   ', evolve.get_scores())
    print('Start best:     ', evolve.get_best_score())
    print('Start solution: ', evolve.get_best_score().get_route())

    evolve.run()

    print('End scores:     ', evolve.get_scores())
    print('End best:       ', evolve.get_best_score())
    print('End solution:   ', evolve.get_best_score().get_route())
    print('*' * 250)


if __name__ == '__main__':
    main()
