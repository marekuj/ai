#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.evolve import Evolve
from src.generation import Generation
from src.random import Random
from src.travel_cost_table import TravelCostTable
from src.unit import Unit


def main():
    cost_min_value = 10
    cost_max_value = 60

    gene_min_value = 0
    gene_max_value = 255
    unit_genes_size = 100
    generation_unit_size = 100
    generation_mutation_chance = 25  # [0-100]
    evolve_delta_stop = 250

    cost_random = Random(cost_min_value, cost_max_value)
    travel_cost_table = TravelCostTable(cost_random, unit_genes_size).create_travel_cost_table_const()

    print(cost_random)
    print(travel_cost_table)

    gene_random = Random(gene_min_value, gene_max_value)
    unit = Unit(gene_random, travel_cost_table, unit_genes_size)
    generation_random = Random(1, unit_genes_size)
    generation = Generation(generation_random, unit, generation_mutation_chance, generation_unit_size)
    evolve = Evolve(generation, evolve_delta_stop)

    print(gene_random)
    print(unit)
    print(generation_random)
    print(generation)
    print(evolve)

    print('*' * 250)
    print('Start scores: ', evolve.get_scores())

    evolve.run()

    print('End scores:   ', evolve.get_scores())
    print('*' * 250)


if __name__ == '__main__':
    main()
