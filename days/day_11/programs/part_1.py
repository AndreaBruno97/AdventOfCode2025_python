from common import *


START_NODE = "you"
END_NODE = "out"


def count_path(start, end, node_dict):
    if start == end:
        return 1

    cur_count = 0

    for next_node in node_dict[start]:
        cur_count += count_path(next_node, end, node_dict)

    return cur_count


class Part_1(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_line_list = open_file_lines(filepath)

        node_dict = dict()

        for file_line_str in file_line_list:
            node_name, output_list_str = file_line_str.split(": ")
            node_dict[node_name] = {x for x in output_list_str.split(" ")}

        return count_path(START_NODE, END_NODE, node_dict)


p1 = Part_1()
p1.test(5)
p1.execute()
