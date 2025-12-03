from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_line_list = open_file_lines(filepath)

        total_joltage = 0

        for line in file_line_list:
            bank = [int(x) for x in line]
            bank_size = len(bank)
            first_max = 0
            first_pos = -1
            second_max = 0

            for cur_battery in range(bank_size-1):
                if bank[cur_battery] > first_max:
                    first_max = bank[cur_battery]
                    first_pos = cur_battery

            for cur_battery in range(first_pos+1, bank_size):
                if bank[cur_battery] > second_max:
                    second_max = bank[cur_battery]

            cur_joltage = (10 * first_max) + second_max
            total_joltage += cur_joltage

        return total_joltage


p1 = Part_1()
p1.test(357)
p1.execute()
