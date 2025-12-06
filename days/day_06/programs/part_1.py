from common import *
import re
import numpy as np

PLUS = "+"
TIMES = "*"


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_lines = open_file_lines(filepath)
        problem_matrix = [
            [y for y in re.split(r'\s+', x.strip())]
            for x in file_lines
        ]
        rows = len(problem_matrix)
        cols = len(problem_matrix[0])

        problem_matrix = np.concatenate(problem_matrix).reshape(rows, cols).T

        grand_total = 0
        for cur_problem in problem_matrix:
            cur_operation = cur_problem[-1]
            cur_operand_list = [int(x) for x in cur_problem[:-1]]

            if cur_operation == PLUS:
                grand_total += sum(cur_operand_list)
            else:
                grand_total += np.prod(cur_operand_list, dtype=object)

        return grand_total


p1 = Part_1()
p1.test(4277556)
p1.execute()
