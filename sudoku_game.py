
import numpy as np
from population import Population

class Sudoku:

    def __init__(self,given):
        self.given = given
        return

    def solve(self, sudoku_given):
        print(self.given) 
        Nc = 1000  # Number of candidates (i.e. population size).

        # Create an initial population.
        self.population = Population()
        self.population.seed(Nc, self.given) # Send Sudoku to population.

