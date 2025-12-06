from common import *
import re
import numpy as np

PLUS = "+"
TIMES = "*"


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_matrix = open_file_str_matrix(filepath)
        rows = len(file_matrix)
        cols = len(file_matrix[0])

        problem_matrix = np.concatenate(file_matrix).reshape(rows, cols).T

        empty_rows_list = [index for index, x in enumerate(problem_matrix == ' ') if x.all()]
        problem_list = [x if index == 0 else x[1:, :] for index, x in
                        enumerate(np.split(problem_matrix, empty_rows_list))]

        grand_total = 0

        for cur_problem in problem_list:
            cur_operation = cur_problem[0, -1]
            cur_operand_matrix = cur_problem[:, :-1]
            cur_operand_list = [int(''.join(x)) for x in cur_operand_matrix]

            if cur_operation == PLUS:
                grand_total += sum(cur_operand_list)
            else:
                grand_total += np.prod(cur_operand_list, dtype=object)

        return grand_total


p2 = Part_2()
p2.test(3263827)
p2.execute()
