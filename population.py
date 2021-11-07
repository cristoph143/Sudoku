
import random
import
from numpy.random.mtrand import randint
from candidate import Candidate
import numpy

Nd = 9  # number of digits


class Population(object):

    def __init__(self, given, NC):
        self.candidates = []
        self.NC = NC
        self.given = given
        return


    def seed(self, Nc, given):
        # initialized population from the number of candidates and given values with heuristic initialization method
        for i in range(0, Nc):
            candidate = Candidate()
            candidate.values = [[0 for j in range(0, Nd)] for i in range(0, Nd)]
            for j in range(0, Nd): # row
                for k in range(0, Nd): # column
                    if given[j][k] == 0: # if the value is not given
                        candidate.values[j][k] = random.randint(1, Nd) # assign random value
                        # check if candidate.values[j][k] is not in the row, column or 3x3 box
                        if self.check_candidate(candidate, j, k) == True:
                            self.candidates.append(candidate)
                        else:
                            k -= 1
                            if k < k - 1:
                                k += 1
                            if k > k + 1:
                                k -= 1
                        # candidate.values[j][k] = random.randint(1, Nd)
                        # self.candidates.append(candidate.values[j][k])
                    else:
                        candidate.values[j][k] = given[j][k]
            self.candidates.append(candidate)
        
    
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
