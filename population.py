
import random
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
                    else:
                        if given[row][column] == 0 and not (self.is_column_duplicate(column, value) or self.is_block_duplicate(row, column, value) or self.is_row_duplicate(row, value)):
                            helper.values[row][column].append(value)
        
        # Seed a new population.       
        for p in range(0, Nc):
            g = Candidate()
            for i in range(0, Nd): # New row in candidate.
                row = numpy.zeros(Nd,dtype=int)
                
                # Fill in the givens.
                for j in range(0, Nd): # New column j value in row i.
                
                    # If value is already given, don't change it.
                    if(given[i][j] != 0):
                        row[j] = given[i][j]
                    # Fill in the gaps using the helper board.
                    elif(given[i][j] == 0):
                        row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j])-1)]

                # If we don't have a valid board, then try again. There must be no duplicates in the row.
                while(len(list(set(row))) != Nd):
                    for j in range(0, Nd):
                        if(given[i][j] == 0):
                            row[j] = helper.values[i][j][random.randint(0, len(helper.values[i][j])-1)]

                g.values[i] = row
            self.candidates.append(g)
        print("Seeding complete.")
        # Compute the fitness of all candidates in the population.
        print('Start\n--------------------------------')
        self.update_fitness()
        print('End\n----------------------------------')
        print("Seeding complete.")
        return

    def is_row_duplicate(self, row, value):
        """ Check whether there is a duplicate of a fixed/given value in a row. """
        for column in range(0, Nd):
            if(self.values[row][column] == value):
                return True
        return False

    def is_column_duplicate(self, column, value):
        """ Check whether there is a duplicate of a fixed/given value in a column. """
        for row in range(0, Nd):
            if(self.values[row][column] == value):
                return True
        return False

    def is_block_duplicate(self, row, column, value):
        """ Check whether there is a duplicate of a fixed/given value in a 3 x 3 block. """
        i = 3*(int(row/3))
        j = 3*(int(column/3))

        if((self.values[i][j] == value)
        or (self.values[i][j+1] == value)
        or (self.values[i][j+2] == value)
        or (self.values[i+1][j] == value)
        or (self.values[i+1][j+1] == value)
        or (self.values[i+1][j+2] == value)
        or (self.values[i+2][j] == value)
        or (self.values[i+2][j+1] == value)
        or (self.values[i+2][j+2] == value)):
            return True
        else:
            return False

    def update_fitness(self):
        # Update fitness of every candidate/chromosome.
        i = 0
        for candidate in self.candidates:
            print(i+1)
            print('---------------------------------------')
            candidate.update_fitness()
            print('---------------------------------------')
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