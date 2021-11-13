
import numpy
from candidate import Candidate
from population import Population
from tournament import Tournament
from cycleCrossover import CycleCrossover

class Sudoku:

    def __init__(self, given):
        self.given = given
        return

    def solve(self, sudoku_given):
        Nc = 10  # Number of candidates (i.e. population size).
        Ne = int(0.1*Nc)  # Number of elites.
        Ng = 10  # Number of generations.

        # Create an initial population.
        self.population = Population(sudoku_given)
        self.population.seed(self.given,Nc)  # Send Sudoku to population.

        # For up to 10000 generations...
        stale = 0
        print('------------Generation---------------')
        for generation in range(0, Ng):
        
            print("Generation %d" % generation)
            # Check for a solution.
            best_fitness = 0.0
            for c in range(0, Nc):
                fitness = self.population.candidates[c].fitness
                print(f'C = {c}  fitness = {fitness}')
                if fitness == 1:
                    print("Solution found at generation %d!" % generation)
                    print(self.population.candidates[c].values)
                    return self.population.candidates[c]

                # Find the best fitness.
                if fitness > best_fitness:
                    best_fitness = fitness
            print("Best fitness: %f" % best_fitness)
        print('-----------End Generation-------------')
            
        # Select elites (the fittest candidates) and preserve them for the next generation.
        self.population.sort()

        print('---------------Elites-----------------')
        print(Ne)
        elites = []
        for e in range(0, Ne):
            elite = Candidate()
            elite.values = numpy.copy(self.population.candidates[e].values)
            elites.append(elite)
        print('-------------End Elites---------------')

        # Create the rest of the candidates.
        print('-------------Tournament---------------')
        for count in range(Ne, Nc, 2):
        # Select parents from population via a tournament.
            t = Tournament()
            parent1 = t.compete(self.population.candidates)
            parent2 = t.compete(self.population.candidates)
            print(f'Parent 1:\n{parent1.values}\nParent 2:\n {parent2.values}')
        print('-----------End Tournament-------------')

        print(f'Final Parent 1:\n{parent1.values}\nFinal Parent 2:\n {parent2.values}')
        # Create the next population.
        next_population = []
        Nm = 0  # Number of mutations.
        
        # Mutation parameters.
        phi = 0
        sigma = 1
        mutation_rate = 0.05

        # Cross-over.
        cc = CycleCrossover()
        print('-------------Crossover---------------')
        child1, child2 = cc.crossover(parent1, parent2, crossover_rate=1.0)
        print('-----------End Crossover-------------')

        print('-------------Mutation---------------')
        # Mutate child1.
        old_fitness = child1.fitness
        print(f'Old:{old_fitness}')
        
        print('---------Child1 Mutating---------------')
        success = child1.mutate(mutation_rate, self.given)
        print(f'Success: {success}')
        child1.update_fitness()
        if(success):
            Nm += 1
            if(child1.fitness > old_fitness):  # Used to calculate the relative success rate of mutations.
                print(f'Child1: {child1.fitness} > Old: {old_fitness}')
                phi = phi + 1
        print('------End Child1 Mutating---------------')
        print(f'Old:{old_fitness}')
        print('---------Child1 Mutating---------------')
        # Mutate child2.
        old_fitness = child2.fitness
        success = child2.mutate(mutation_rate, self.given)
        print(f'Success: {success}')
        child2.update_fitness()
        if(success):
            Nm += 1
            if(child2.fitness > old_fitness):  # Used to calculate the relative success rate of mutations.
                print(f'Child1: {child1.fitness} > Old: {old_fitness}')
                phi = phi + 1
        print('------End Child2 Mutating---------------')
                
        # Add children to new population.
        next_population.append(child1)
        next_population.append(child2)
        # Append elites onto the end of the population. These will not have been affected by crossover or mutation.
        for e in range(0, Ne):
            next_population.append(elites[e])
                
        # Select next generation.
        self.population.candidates = next_population
        self.population.update_fitness()
            
        # Calculate new adaptive mutation rate (based on Rechenberg's 1/5 success rule). This is to stop too much mutation as the fitness progresses towards unity.
        if(Nm == 0):
            phi = 0  # Avoid divide by zero.
        else:
            phi = phi / Nm
            
        if(phi > 0.2):
            sigma = sigma/0.998
        elif(phi < 0.2):
            sigma = sigma*0.998

        mutation_rate = abs(numpy.random.normal(loc=0.0, scale=sigma, size=None))
        Nm = 0
        phi = 0

        # Check for stale population.
        self.population.sort()
        if(self.population.candidates[0].fitness != self.population.candidates[1].fitness):
            stale = 0
        else:
            stale += 1
        print('-------------End Mutation---------------')
        return None