from common import *


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):
        input_str = open_file(filepath)

        range_list_str, _ = input_str.split("\n\n")
        range_list = [[int(y) for y in x.split("-")] for x in range_list_str.split("\n")]

        # Packing ranges
        # Each range is split into a triplet (value, index, isStart)
        # a-b becomes (a, 0, True), (b, 0, False)

        edge_list = []
        for cur_index, cur_range in enumerate(range_list):
            edge_list.append((cur_range[0], cur_index, True))
            edge_list.append((cur_range[1], cur_index, False))

        # Edges are sorted by the value they contain
        edge_list.sort(key=lambda x: x[0])

        # A packed range starts when the first Start edge is found,
        # and for each Start edge found until the end, the corresponding
        # End edge must be found (by index)
        total_fresh = 0
        index_set = set()
        start_edge = -1
        # Variable that keeps track if a previous packed range ends with
        # the same value as the start of the following range
        last_end = -1
        for cur_edge, cur_index, isStart in edge_list:
            if isStart:
                # Start edge
                if len(index_set) == 0:
                    start_edge = cur_edge
                index_set.add(cur_index)
            else:
                # End edge
                index_set.remove(cur_index)
                if len(index_set) == 0:
                    total_fresh += (cur_edge - start_edge + 1)
                    if last_end == start_edge:
                        total_fresh -= 1

                    last_end = cur_edge

        return total_fresh


p2 = Part_2()
p2.test(14)
p2.execute()
