from common import *
import numpy as np
from scipy.optimize import linprog
import re

LIGHT_ON = "#"
LIGHT_OFF = "."


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        machine_list = open_file_lines(filepath)

        machine_pattern = r'\[(.+)\] (.*) \{(.+)\}'

        press_total = 0
        for machine_str in machine_list:
            light_list_str, button_list_str, joltage_list_str = re.findall(machine_pattern, machine_str)[0]

            button_list = [
                [int(value) for value in button_str.split(",")]
                for button_str in button_list_str.replace("(", "").replace(")", "").split(" ")
            ]
            joltage_list = [int(value) for value in joltage_list_str.split(",")]

            equation_system_matrix = []
            solution_matrix = []
            for cur_row in range(len(joltage_list)):
                equation_system_matrix.append(
                    [1 if cur_row in button else 0 for button in button_list]
                )
                solution_matrix.append(joltage_list[cur_row])

            A_eq = np.array(equation_system_matrix)
            b_eq = np.array(solution_matrix)
            c = np.ones(len(button_list))
            bounds = [(0, None)] * len(button_list)

            res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
            cur_button_press = int(res.fun)
            press_total += cur_button_press

        return press_total


p2 = Part_2()
p2.test(33)
p2.execute()
