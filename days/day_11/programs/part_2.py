from common import *


START_NODE = "svr"
END_NODE = "out"
DAC_NODE = "dac"
FFT_NODE = "fft"


def count_path(start, end, node_dict, path_count_dict):
    path_count_key = start+end

    if path_count_key in path_count_dict.keys():
        return path_count_dict[path_count_key]

    cur_count = 0

    if start == end:
        cur_count = 1
    else:
        for next_node in node_dict[start]:
            cur_count += count_path(next_node, end, node_dict, path_count_dict)

    path_count_dict[path_count_key] = cur_count
    return cur_count


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        file_line_list = open_file_lines(filepath)

        if "example.txt" in filepath:
            # Part 1 example is not compatible with part 2
            return -1

        node_dict = dict()

        for file_line_str in file_line_list:
            node_name, output_list_str = file_line_str.split(": ")
            node_dict[node_name] = {x for x in output_list_str.split(" ")}

        node_dict[END_NODE] = set()

        # Memory for paths that are already discovered
        path_count_dict = {}

        # "svt" to "out" passing from "dac" and "fft"
        # Only two ways:
        #   svt -> dac -> fft -> out
        #   svt -> fft -> dac -> out

        svt_dac = count_path(START_NODE, DAC_NODE, node_dict, path_count_dict)
        dac_fft = count_path(DAC_NODE, FFT_NODE, node_dict, path_count_dict)
        fft_out = count_path(FFT_NODE, END_NODE, node_dict, path_count_dict)

        first_total = svt_dac * dac_fft * fft_out

        svt_fft = count_path(START_NODE, FFT_NODE, node_dict, path_count_dict)
        fft_dac = count_path(FFT_NODE, DAC_NODE, node_dict, path_count_dict)
        dac_out = count_path(DAC_NODE, END_NODE, node_dict, path_count_dict)

        second_total = svt_fft * fft_dac * dac_out

        return first_total + second_total


p2 = Part_2()
p2.test(-1, [("example_2.txt", 2)])
p2.execute()
