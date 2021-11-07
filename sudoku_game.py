
import numpy as np
from population import Population


class Sudoku:

    def __init__(self, given):
        self.given = given
        return

    def solve(self, sudoku_given):
        Nc = 5  # Number of candidates (i.e. population size).
        
        Ne = int(0.05*Nc)  # Number of elites.
        Ng = 1000  # Number of generations.
        Nm = 0  # Number of mutations.

        # Create an initial population.
        self.population = Population(self.given, Nc)
        self.population.seed(Nc, self.given)  # Send Sudoku to population.

        # Create a list of all the solutions.
        self.solutions = []