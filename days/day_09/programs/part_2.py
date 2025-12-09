from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        tile_list = [[int(x) for x in tile_str.split(",")] for tile_str in open_file_lines(filepath)]
        tile_num = len(tile_list)

        horizontal_line_list = []
        vertical_line_list = []

        # Edge construction
        for cur_index in range(tile_num):
            cur_x, cur_y = tile_list[cur_index]
            next_x, next_y = tile_list[(cur_index + 1) % tile_num]

            if cur_x == next_x:
                vertical_line_list.append([cur_x, cur_y, next_y])
            else:
                horizontal_line_list.append([cur_y, cur_x, next_x])

        max_area = 0

        for index_1 in range(tile_num):
            for index_2 in range(index_1 + 1, tile_num):
                x_1, y_1 = tile_list[index_1]
                x_2, y_2 = tile_list[index_2]

                min_x = min(x_1, x_2)
                max_x = max(x_1, x_2)
                min_y = min(y_1, y_2)
                max_y = max(y_1, y_2)

                # Check vertical intersection
                if any(min_x <= h_x <= max_x and (min_y <= h_y_1 <= max_y or min_y <= h_y_2 <= max_y)
                       for h_x, h_y_1, h_y_2 in vertical_line_list):
                    continue

                # Check horizontal intersection
                if any(min_y <= h_y <= max_y and (min_x <= h_x_1 <= max_x or min_x <= h_x_2 <= max_x)
                       for h_y, h_x_1, h_x_2 in horizontal_line_list):
                    continue

                cur_area = abs(x_1 - x_2 + 1) * abs(y_1 - y_2 + 1)
                if cur_area > max_area:
                    max_area = cur_area

        return max_area


p2 = Part_2()
p2.test(24)
# p2.execute()
