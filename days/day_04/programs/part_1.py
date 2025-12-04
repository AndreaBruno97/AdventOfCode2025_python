from common import *
import numpy as np

PAPER = "@"
EMPTY = "."
MAX_NEAR = 3


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        grid = open_file_str_matrix_guarded(filepath, EMPTY)
        cols = len(grid)
        rows = len(grid[0])
        total_paper = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if grid[r][c] == EMPTY:
                    continue

                submatrix = grid[r-1:r+2, c-1:c+2]
                total_near = np.count_nonzero(submatrix == PAPER)
                total_near -= 1  # Not counting the paper itself in the middle

                if total_near <= MAX_NEAR:
                    total_paper += 1

        return total_paper


p1 = Part_1()
p1.test(13)
p1.execute()
