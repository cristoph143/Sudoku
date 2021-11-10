import numpy

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

        for i in range(0, Nd):  # For each row...
            for j in range(0, Nd):  # For each number within it...
                # ...Update list with occurrence of a particular number.
                row_count[self.values[i][j]-1] += 1

            row_sum += (1.0/len(set(row_count)))/Nd
            print(f'Row Sum: {row_sum} += (1.0/{len(set(row_count))})/{Nd}')
            row_count = numpy.zeros(Nd)
        
        print('---------------------------------------')

        for i in range(0, Nd):  # For each column...
            for j in range(0, Nd):  # For each number within it...
                # ...Update list with occurrence of a particular number.
                column_count[self.values[j][i]-1] += 1

            column_sum += (1.0 / len(set(column_count)))/Nd
            print(f'Column Sum: {column_sum} += (1.0/{len(set(column_count))})/{Nd}')
            column_count = numpy.zeros(Nd)

        
        print('---------------------------------------')

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
                print(f'Block Sum: {block_sum} += (1.0/{len(set(block_count))})/{Nd}')
                block_sum += (1.0/len(set(block_count)))/Nd
                block_count = numpy.zeros(Nd)
        
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