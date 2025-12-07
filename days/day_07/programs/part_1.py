from common import *


START = "S"
EMPTY = "."
SPLIT = "^"


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        manifold = open_file_str_matrix(filepath)
        rows = len(manifold)
        cols = len(manifold[0])

        # Set of column positions for each beam
        beam_set = set()
        # Set of row/column coordinates for each split
        split_set = set()

        for r in range(rows):
            for c in range(cols):
                if manifold[r][c] == START:
                    beam_set.add(c)
                elif manifold[r][c] == SPLIT:
                    split_set.add((r, c))

        split_count = 0

        for r in range(rows):
            new_beam_set = set()
            for beam in beam_set:
                if (r, beam) in split_set:
                    split_count += 1
                    new_beam_set.add(beam-1)
                    new_beam_set.add(beam+1)
                else:
                    new_beam_set.add(beam)
            beam_set = new_beam_set

        return split_count


p1 = Part_1()
p1.test(21)
p1.execute()
