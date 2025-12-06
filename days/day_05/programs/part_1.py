from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_str = open_file(filepath)

        range_list_str, id_list_str = input_str.split("\n\n")
        range_list = [[int(y) for y in x.split("-")] for x in range_list_str.split("\n")]
        id_list = [int(x) for x in id_list_str.split("\n")]

        total_fresh = 0

        for cur_id in id_list:
            for cur_range in range_list:
                if cur_range[0] <= cur_id <= cur_range[1]:
                    total_fresh += 1
                    break

        return total_fresh


p1 = Part_1()
p1.test(3)
p1.execute()
