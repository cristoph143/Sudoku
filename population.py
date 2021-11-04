
import random
from candidate import Candidate
import numpy

Nd = 9  # number of digits


class Population(object):

    def __init__(self):
        self.candidates = []
        return

    def seed(self, Nc, given):
        self.candidates = []

        # Determine the legal values that each square can take.
        helper = Candidate()
        helper.values = [
            [
                []
                for j in range(0, Nd)
            ]
            for i in range(0, Nd)
        ]
        for row in range(0, Nd):
            for column in range(0, Nd):
                for value in range(1, 10):  # cell 1 - 9
                    print('row column value')
                    print(f'{row}\t{column}\t{value}')
