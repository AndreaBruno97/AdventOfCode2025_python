from common import *
import re
import itertools

LIGHT_ON = "#"
LIGHT_OFF = "."


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        machine_list = open_file_lines(filepath)

        machine_pattern = r'\[(.+)\] (.*) \{(.+)\}'

        press_total = 0
        for machine_str in machine_list:
            light_list_str, button_list_str, joltage_list_str = re.findall(machine_pattern, machine_str)[0]

            light_list = [True if x == LIGHT_ON else False for x in light_list_str]
            button_list = [
                [int(value) for value in button_str.split(",")]
                for button_str in button_list_str.replace("(", "").replace(")", "").split(" ")
            ]

            is_found = False
            for combination_len in range(len(button_list)):
                for cur_combination in itertools.combinations(button_list, combination_len):

                    cur_light_list = [False] * len(light_list)
                    for cur_button in cur_combination:
                        for cur_light in cur_button:
                            cur_light_list[cur_light] = not cur_light_list[cur_light]

                    if light_list == cur_light_list:
                        is_found = True
                        press_total += len(cur_combination)
                        break

                if is_found:
                    break

        return press_total


p1 = Part_1()
p1.test(7)
p1.execute()
