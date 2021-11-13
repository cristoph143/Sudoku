import random
random.seed()
from numpy.random.mtrand import randint
from candidate import Candidate
import numpy
from functools import cmp_to_key

Nd = 9  # number of digits
class Population(object):

    def __init__(self, given):
        self.candidates = []
        self.values = given

        return

    def seed(self, given, Nc):
        self.candidates = []
        helper = Candidate()
        helper.values = [[[] for j in range(0, Nd)] for i in range(0, Nd)]
        for row in range(0, Nd):
            for column in range(0, Nd):
                for value in range(1, Nd + 1):
                    if given[row][column] != 0:
                        # Given/known value from file.
                        helper.values[row][column] = given[row][column]
                        break
                    elif (given[row][column] == 0 
                            and not helper.is_column_duplicate(column, value) 
                            or helper.is_block_duplicate(row, column, value) 
                            or helper.is_row_duplicate(row, value)):
                        helper.values[row][column].append(value)

        # Seed a new population.
        for p in range(0, Nc):
            g = Candidate()

            for i in range(0, Nd):  # New row in candidate.
                row = numpy.zeros(Nd, dtype=int)
                # Fill in the givens.
                for j in range(0, Nd):  # New column j value in row i.
                    # If value is already given, don't change it.
                    if(given[i][j] != 0):
                        row[j] = given[i][j]
                    # Fill in the gaps using the helper board.
                    elif(given[i][j] == 0):
                        row[j] = helper.values[i][j][random.randint(
                            0, len(helper.values[i][j])-1)]
                # If we don't have a valid board, then try again. There must be no duplicates in the row.
                while(len(list(set(row))) != Nd):
                    for j in range(0, Nd):
                        if(given[i][j] == 0):
                            row[j] = helper.values[i][j][random.randint(
                                0, len(helper.values[i][j])-1)]
                g.values[i] = row
            self.candidates.append(g)

        # Compute the fitness of all candidates in the population.
        print('-------------Start------------------')
        self.update_fitness()
        print('--------------End--------------------')
        print("Seeding complete.")
        return

    def update_fitness(self):
        # Update fitness of every candidate/chromosome.
        i = 0
        for candidate in self.candidates:
            print('----------Update Fitness---------------')
            print(f'Candidate {i+1}')
            candidate.update_fitness()
            print('--------End Update Fitness-------------')
            i += 1
        return

    def sort(self):
        print(self.candidates.sort(key=cmp_to_key(self.sort_fitness)))
        return

    def sort_fitness(self, x, y):
        if(x.fitness < y.fitness):
            return 1
        elif(x.fitness == y.fitness):
            return 0
        else:
            return -1
