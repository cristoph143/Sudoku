from candidate import Candidate
import numpy
import random

Nd = 9

class CycleCrossover(object):

    def __init__(self):
        return
    
    def crossover(self, parent1, parent2, crossover_rate):
        """ Create two new child candidates by crossing over parent genes. """
        child1 = Candidate()
        child2 = Candidate()
        
        # Make a copy of the parent genes.
        child1.values = numpy.copy(parent1.values)
        child2.values = numpy.copy(parent2.values)
        print(f'Child1:\n{child1.values}\nChild2:\n{child2.values}\n')

        r = random.uniform(0, 1.1)
        while(r > 1):  # Outside [0, 1] boundary. Choose another.
            r = random.uniform(0, 1.1)
            print(f'r: {r}')
            
        # Perform crossover.
        if (r < crossover_rate):
            # Pick a crossover point. Crossover must have at least 1 row (and at most Nd-1) rows.
            crossover_point1 = random.randint(0, 8)
            crossover_point2 = random.randint(1, 9)
            while(crossover_point1 == crossover_point2):
                crossover_point1 = random.randint(0, 8)
                crossover_point2 = random.randint(1, 9)
                print(f'Crossover point1: {crossover_point1}')
                print(f'Crossover point2: {crossover_point2}')

                
            if(crossover_point1 > crossover_point2):
                temp = crossover_point1
                crossover_point1 = crossover_point2
                crossover_point2 = temp
                
            for i in range(crossover_point1, crossover_point2):
                child1.values[i], child2.values[i] = self.crossover_rows(child1.values[i], child2.values[i])
                print(f'Child1:\n{child1.values}\nChild2:\n{child2.values}\n')

        return child1, child2

    # using uniform crossover in crossover between two parents row
    def crossover_rows(self, parent1_row, parent2_row):
        """ Crossover between two parents row. """
        child1_row = numpy.copy(parent1_row)
        child2_row = numpy.copy(parent2_row)
        print(f'Child1 row:\n{child1_row}\nChild2 row:\n{child2_row}\n')
        
        # Find unused values in parent1_row.
        unused = []
        for i in range(0, len(parent1_row)):
            if(parent1_row[i] not in parent2_row):
                unused.append(parent1_row[i])
                print(f'Unused: {unused}')
        
        # Find unused values in parent2_row.
        for i in range(0, len(parent2_row)):
            if(parent2_row[i] not in parent1_row):
                unused.append(parent2_row[i])
                print(f'Unused: {unused}')
        
        # Find unused values in parent1_row.
        for i in range(0, len(unused)):
            child1_row[self.find_unused(child1_row, unused)] = unused[i]
            child2_row[self.find_unused(child2_row, unused)] = unused[i]
            print(f'Child1 row:\n{child1_row}\nChild2 row:\n{child2_row}\n')
        
        return child1_row, child2_row


    def find_unused(self, parent_row, remaining):
        for i in range(0, len(parent_row)):
            if(parent_row[i] in remaining):
                print(f'Remaining: {remaining}')
                return i

    def find_value(self, parent_row, value):
        for i in range(0, len(parent_row)):
            if(parent_row[i] == value):
                print(f'{parent_row[i]} == {value}')
                return i