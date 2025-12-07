from common import *


START = "S"
EMPTY = "."
SPLIT = "^"


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        manifold = open_file_str_matrix(filepath)
        rows = len(manifold)
        cols = len(manifold[0])

        # Dictionary of column positions for each beam (value is the number of occurrences)
        beam_dict = {}
        # Set of row/column coordinates for each split
        split_set = set()

        for r in range(rows):
            for c in range(cols):
                if manifold[r][c] == START:
                    beam_dict[c] = 1
                elif manifold[r][c] == SPLIT:
                    split_set.add((r, c))

        for r in range(rows):
            new_beam_dict = {}
            for beam in beam_dict.keys():

                if (r, beam) in split_set:
                    new_left = new_beam_dict.get(beam-1) or 0
                    new_right = new_beam_dict.get(beam+1) or 0
                    new_beam_dict[beam-1] = new_left + beam_dict[beam]
                    new_beam_dict[beam+1] = new_right + beam_dict[beam]
                else:
                    new_num = new_beam_dict.get(beam) or 0
                    new_beam_dict[beam] = new_num + beam_dict[beam]
            beam_dict = new_beam_dict

        return sum(beam_dict.values())


p2 = Part_2()
p2.test(40)
p2.execute()
