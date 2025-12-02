from common import *


class Part_2(BaseClass):

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

                for block_len in range(1, int(cur_id_len/2)+1):
                    repeat_times = int(cur_id_len/block_len)
                    if cur_id_str[0:block_len] * repeat_times == cur_id_str:
                        invalid_id_total += cur_id
                        break

        return invalid_id_total


p2 = Part_2()
p2.test(4174379265)
p2.execute()
