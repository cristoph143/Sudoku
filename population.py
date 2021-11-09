
import random
from numpy.random.mtrand import randint
from candidate import Candidate
import numpy

Nd = 9  # number of digits


class Population(object):

    def __init__(self,given,Nc):
        self.candidates = []
        self.population = []
        self.values = given
        self.num_can = Nc
        self.bestPop = []
        return

    # call seed function to get candidates and saved to initialized population
    def initialize(self, Nc, given):
        self.candidates =  []
        for generation in range(0, Nc):
            self.seed(given)
            self.population.append(self.candidates)
        return

    def seed(self, given):
        self.candidates = [] 

        # Determine the legal values that each square can take.
        helper = Candidate()
        helper.values = [[0 for j in range(0, Nd)] for i in range(0, Nd)]
        for row in range(0, Nd):
            for column in range(0, Nd): 
                if given[row][column] == 0: 
                    # helper.values[row][column] = random.randint(1, Nd)
                    # print(helper.values[row][column])
                    if self.check_candidate(helper, row, column) == True:
                        # Value is available.
                        helper.values[row][column]
                        print(helper.values[row][column])
                    else:
                        helper.values[row][column] = random.randint(1, Nd)
                        print(helper.values[row][column])
                        column -= 1
                        if column < column - 1:
                            column += 1
                        if column > column + 1:
                            column -= 1
                elif(given[row][column] != 0):
                    # Given/known value from file.
                    helper.values[row][column] = given[row][column]
        fitness = self.fitness(helper)
        # for row1 in range(0, Nd):
        #     for column1 in range(0, Nd):
        #         self.check_candidate(helper, row1, column1)
        
        # Compute the fitness of all candidates in the population.
        # self.update_fitness()
        print("Seeding complete.")
        return

    def fitness(self, candidate):
        # Compute the fitness of a candidate.
        fitness = 0
        for row in range(0, Nd):
            for column in range(0, Nd):
                if candidate.values[row][column] == self.values[row][column]:
                    fitness += 1
        return fitness
    
    def check_candidate(self, candidate, j, k):
        # check if candidate.values[j][k] is not in the row, column or 3x3 box
        for i in range(0, Nd):
            if i != j: # row
                if candidate.values[i][k] == candidate.values[j][k]:
                    return False
        for i in range(0, Nd):
            if i != k: # column
                if candidate.values[j][i] == candidate.values[j][k]:
                    return False
        for i in range(0, Nd):
            if i != j: # box
                if i != k:
                    if candidate.values[i][i] == candidate.values[j][k]:
                        return False
        return True

    def update_fitness(self):
        # Compute the fitness of all candidates in the population.
        for candidate in self.candidates:
            candidate.fitness = self.fitness(candidate)
        return
