import numpy
import random

Nd = 9  # number of digits


class Candidate(object):

    def __init__(self):
        self.values = numpy.zeros((Nd, Nd), dtype=int) # Set the 9x9 Sudoku into 0s
        self.fitness = None
        return

    def update_fitness(self):

        row_count = numpy.zeros(Nd,dtype=int)
        column_count = numpy.zeros(Nd,dtype=int)
        block_count = numpy.zeros(Nd,dtype=int)
        row_sum = 0
        column_sum = 0
        block_sum = 0

        
        print('--------------Row Sum--------------------')
        for i in range(0, Nd):  # For each row...
            for j in range(0, Nd):  # For each number within it...
                # ...Update list with occurrence of a particular number.
                row_count[self.values[i][j]-1] += 1

            row_sum += (1.0/len(set(row_count)))/Nd
            print(f'{row_sum} += (1.0/{len(set(row_count))})/{Nd}')
            row_count = numpy.zeros(Nd)
        
        print('-------------Column Sum------------------')

        for i in range(0, Nd):  # For each column...
            for j in range(0, Nd):  # For each number within it...
                # ...Update list with occurrence of a particular number.
                column_count[self.values[j][i]-1] += 1

            column_sum += (1.0 / len(set(column_count)))/Nd
            print(f'{column_sum} += (1.0/{len(set(column_count))})/{Nd}')
            column_count = numpy.zeros(Nd)
        
        print('-------------Block Sum--------------------')

        # For each block...
        for i in range(0, Nd, 3):
            for j in range(0, Nd, 3):
                block_count[self.values[i][j]-1] += 1
                block_count[self.values[i][j+1]-1] += 1
                block_count[self.values[i][j+2]-1] += 1

                block_count[self.values[i+1][j]-1] += 1
                block_count[self.values[i+1][j+1]-1] += 1
                block_count[self.values[i+1][j+2]-1] += 1

                block_count[self.values[i+2][j]-1] += 1
                block_count[self.values[i+2][j+1]-1] += 1
                block_count[self.values[i+2][j+2]-1] += 1
                block_sum += (1.0/len(set(block_count)))/Nd
                print(f'{block_sum} += (1.0/{len(set(block_count))})/{Nd}')
                block_count = numpy.zeros(Nd)
        
        print('------------Overall Fitness--------------------')
        # Calculate overall fitness.
        if (int(row_sum) == 1 and int(column_sum) == 1 and int(block_sum) == 1):
            fitness = 1.0
            print(f'Row Sum = {row_sum} Column Sum = {column_sum} Block Sum = {block_sum} Fitness = {fitness}')
        else:
            fitness = column_sum * block_sum
            print('Fitness =\t\t Column Sum\t * Block Sum')
            print(f'{fitness} = {column_sum} * {block_sum}')
        self.fitness = fitness
        return

    def mutate(self, mutation_rate, given):
        """ Mutate a candidate by picking a row, and then picking two values within that row to swap. """

        r = random.uniform(0, 1.1)
        while(r > 1): # Outside [0, 1] boundary - choose another
            r = random.uniform(0, 1.1)
            print(f'r = {r}')
    
        success = False
        if (r < mutation_rate):  # Mutate.
            while(not success):
                row1 = random.randint(0, 8)
                row2 = random.randint(0, 8)
                row2 = row1
                print(f'row1 = {row1} row2 = {row2}')
                
                from_column = random.randint(0, 8)
                to_column = random.randint(0, 8)
                while(from_column == to_column):
                    from_column = random.randint(0, 8)
                    to_column = random.randint(0, 8)   
                # Check if the two places are free...
                if(given[row1][from_column] == 0 and given[row1][to_column] == 0):
                    # ...and that we are not causing a duplicate in the rows' columns.
                    if self.is_column_duplicate(to_column, self.values[row1][from_column]): return
                    if self.is_column_duplicate(from_column, self.values[row2][to_column]): return
                    if self.is_block_duplicate(row2, to_column, self.values[row1][from_column]): return
                    if self.is_block_duplicate(row1, from_column, self.values[row2][to_column]): return
                    # Swap values.
                    temp = self.values[row2][to_column]
                    self.values[row2][to_column] = self.values[row1][from_column]
                    self.values[row1][from_column] = temp
                    success = True
    
        return success

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