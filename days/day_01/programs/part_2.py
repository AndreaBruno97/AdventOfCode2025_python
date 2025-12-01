from common import *
import math

DIAL_SIZE = 100
DIAL_START = 50
LEFT = "L"
RIGHT = "R"


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_lines = open_file_lines(filepath)

        cur_pos = DIAL_START
        zero_count = 0

        for input_line in input_lines:
            direction = input_line[0]
            distance = int(input_line[1:])

            for i in range(distance):
                delta = 1 if direction == RIGHT else -1

                cur_pos = (cur_pos + delta) % DIAL_SIZE

                if cur_pos == 0:
                    zero_count += 1

        return zero_count


p2 = Part_2()
p2.test(6)
p2.execute()
