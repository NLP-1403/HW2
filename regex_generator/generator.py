"""
Genetic Algorithm-Based Regex Generator

This module implements a genetic algorithm to automatically generate optimized
regular expression patterns from example strings. The algorithm evolves a
population of regex patterns over multiple generations, selecting the fittest
patterns based on how well they match the input examples.

Key Features:
- Population-based evolution with configurable size
- 21 distinct gene types representing regex building blocks
- Fitness-based selection and crossover
- Returns top-3 best-performing patterns

Algorithm Flow:
1. Initialize random population of gene sequences
2. Evaluate fitness of each pattern against examples
3. Select best performers and create next generation
4. Repeat for specified number of generations
5. Return top-3 patterns sorted by fitness score

Functions:
    generator(target, POPULATION, GENERATION, match): Main entry point
        - target: List of example strings to match
        - POPULATION: Number of patterns per generation (e.g., 100)
        - GENERATION: Number of evolution cycles (e.g., 10)
        - match: Number of examples to use per evaluation (default: all)

Example:
    >>> from regex_generator.generator import generator
    >>> examples = ["test123", "demo456", "sample789"]
    >>> patterns = generator(examples, population=100, generation=10)
    >>> print(patterns)  # [(0.95, r'[a-z]+\d{3}'), ...]
"""

from .parser import *
from .genetic import genotype, nextGeneration
from .parser import *


def generator(target, POPULATION, GENERATION, match=None):
    g = 1
    result = []
    if match == None or match > len(target):
        match = len(target)
    gene_count = len(genotype)
    pop = [random.sample(range(0, gene_count), gene_count) for _ in range(POPULATION)]
    for i in range(GENERATION):

        MAX_FITNESS = -1e9
        BEST_GENE = None
        BEST_REGEX = ""
        # Get result
        arr, filtered_set = preprocessor(random.sample(target, match))
        current_generation = []
        for idx, gene in enumerate(pop):
            g_res, fitness = parser(arr, filtered_set, gene)
            result.append((fitness, ''.join(g_res)))
            current_generation.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        print(f'{i} Generation :')
        print(f'{MAX_FITNESS} {BEST_REGEX}')

        # Next generation
        fitness = [g[0] for g in current_generation]
        pop = nextGeneration(pop, fitness)

    return result


if __name__ == "__main__":

    POPULATION = 100
    GENERATION = 2
    import sys

    target = open(sys.argv[1], 'r').read().split('\n')

    # print("\nTarget :\n\t", end='')
    # print('\n\t'.join(target), end='\n\n')

    result = []

    result = generator(target, POPULATION, GENERATION)

    for fit, regex in sorted(set(result), key=lambda x: -x[0])[:20]:
        print(f'{fit}\t\t{regex}')
