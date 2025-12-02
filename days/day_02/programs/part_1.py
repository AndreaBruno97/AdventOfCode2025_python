from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        range_line_list = open_file(filepath).split(",")

        invalid_id_total = 0

        for range_line in range_line_list:
            range_min, range_max = [int(x) for x in range_line.split("-")]

            for cur_id in range(range_min, range_max + 1):
                cur_id_str = str(cur_id)
                cur_id_len = len(cur_id_str)
                cur_half_point = int(cur_id_len/2)

                if cur_id_str[0:cur_half_point] == cur_id_str[cur_half_point:]:
                    invalid_id_total += cur_id

        return invalid_id_total


p1 = Part_1()
p1.test(1227775554)
p1.execute()
