
import numpy as np
from candidate import Candidate
from population import Population


class Sudoku:

    def __init__(self, given):
        self.given = given
        return

    def solve(self, sudoku_given):
        Nc = 5  # Number of candidates (i.e. population size).
        Ne = int(0.05*Nc)  # Number of elites.
        Ng = 10  # Number of generations.

        # Create an initial population.
        self.population = Population(sudoku_given)
        self.population.seed(self.given,Nc)  # Send Sudoku to population.

        # For up to 10000 generations...
        stale = 0
        for generation in range(0, Ng):
        
            print("Generation %d" % generation)
            # Check for a solution.
            best_fitness = 0.0
            for c in range(0, Nc):
                fitness = self.population.candidates[c].fitness
                print(f'C = {c}  fitness = {fitness}')
                if(fitness == 1):
                    print("Solution found at generation %d!" % generation)
                    print(self.population.candidates[c].values)
                    return self.population.candidates[c]

                # Find the best fitness.
                if(fitness > best_fitness):
                    best_fitness = fitness

            print("Best fitness: %f" % best_fitness)
            
        # Create the next population.
        next_population = []

        # Select elites (the fittest candidates) and preserve them for the next generation.
        self.population.sort()
        elites = []
        for e in range(0, Ne):
            elite = Candidate()
            elite.values = np.copy(self.population.candidates[e].values)
            elites.append(elite)