import numpy

Nd = 9  # number of digits


class Candidate(object):

    def __init__(self):
        self.values = numpy.zeros((Nd, Nd), dtype=int) # Set the 9x9 Sudoku into 0s
        print(self.values)
        return
