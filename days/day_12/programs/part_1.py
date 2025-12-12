from common import *

FULL = "#"
EMPTY = "."


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_str = open_file(filepath)

        file_str_list = file_str.split("\n\n")
        shape_list_string = file_str_list[:-1]
        region_list_str = file_str_list[-1]

        shape_list = [[
            [z == FULL for z in list(y)]
            for y in x.split(":\n")[1].split("\n")]
            for x in shape_list_string]

        size_list = [
            sum([y.count(FULL) for y in x.split(":\n")[1]])
            for x in shape_list_string]

        region_list = []
        for region_str in region_list_str.split("\n"):
            size_str, shape_list_str = region_str.split(": ")
            cols, rows = [int(x) for x in size_str.split("x")]
            shape_list = [int(x) for x in shape_list_str.split(" ")]
            region_list.append([rows, cols, shape_list])

        possible_fit_count = 0
        for rows, cols, cur_shape_list in region_list:
            region_size = rows * cols
            max_size = sum([size * count for size, count in zip(size_list, cur_shape_list)])
            if region_size >= max_size:
                possible_fit_count += 1

        return possible_fit_count


p1 = Part_1()
p1.test(2)
p1.execute()
