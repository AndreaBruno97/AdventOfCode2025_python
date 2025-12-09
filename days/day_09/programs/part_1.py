from common import *


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        tile_list = [[int(x) for x in tile_str.split(",")] for tile_str in open_file_lines(filepath)]
        tile_num = len(tile_list)

        max_area = 0

        for index_1 in range(tile_num):
            for index_2 in range(index_1+1, tile_num):
                x_1, y_1 = tile_list[index_1]
                x_2, y_2 = tile_list[index_2]

                cur_area = abs(x_1 - x_2 + 1) * abs(y_1 - y_2 + 1)
                if cur_area > max_area:
                    max_area = cur_area

        return max_area


p1 = Part_1()
p1.test(50)
p1.execute()
