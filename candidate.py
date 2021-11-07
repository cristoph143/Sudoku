import numpy

Nd = 9  # number of digits


class Candidate(object):

    def __init__(self):
        self.values = numpy.zeros((Nd, Nd), dtype=int) # Set the 9x9 Sudoku into 0s
        return

    # function that randomizes the popul

    def randomize_with_given_and_given_row_and_given_column_and_given_box_and_given_box_and_given_column(self,given):
        for i in range(Nd):
            for j in range(Nd):
                self.values[i, j] = numpy.random.randint(1, 10)
                print = self.values[i, j]
        return