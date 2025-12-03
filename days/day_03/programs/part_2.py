from common import *

BATTERY_NUM = 12


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_line_list = open_file_lines(filepath)

        total_joltage = 0

        for line in file_line_list:
            bank = [int(x) for x in line]
            bank_size = len(bank)
            start_battery = -1
            cur_joltage = 0

            for cur_iteration in range(BATTERY_NUM, 0, -1):  # from BATTERY_NUM to 1
                end_battery = bank_size - cur_iteration + 1
                cur_max_battery = 0

                for cur_battery in range(start_battery+1, end_battery):
                    if bank[cur_battery] > cur_max_battery:
                        cur_max_battery = bank[cur_battery]
                        start_battery = cur_battery

                cur_joltage = (10 * cur_joltage) + cur_max_battery

            total_joltage += cur_joltage

        return total_joltage


p2 = Part_2()
p2.test(3121910778619)
p2.execute()
