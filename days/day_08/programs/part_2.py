from common import *
import math

MAX_STEPS_TEST = 10
MAX_STEPS = 1000


def get_set(circuit_list: list[set[str]], box: str):
    valid_sets = [x for x in circuit_list if box in x]
    if len(valid_sets) == 0:
        return None
    return valid_sets[0]


class Part_2(BaseClass):

    def __init__(self):
        super().__init__()

    def execute_internal(self, filepath):

        if "example.txt" in filepath:
            cur_max_steps = MAX_STEPS_TEST
        else:
            cur_max_steps = MAX_STEPS

        box_str_list = open_file_lines(filepath)
        box_list = [[int(x) for x in box_str.split(",")] + [box_str] for box_str in box_str_list]
        box_num = len(box_list)

        # Computing box distances
        # box_distance is an array of pairs: set of two boxes and distance between them
        # ordered by increasing distance
        # [[{'162,817,812', '425,690,689'}, 316.90219311326956], ...]

        box_distance = []

        for first_box in range(box_num):
            for second_box in range(first_box + 1, box_num):
                x_1, y_1, z_1, box_1 = box_list[first_box]
                x_2, y_2, z_2, box_2 = box_list[second_box]
                box_distance.append([
                    {box_1, box_2},
                    math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2) + math.pow(z_1 - z_2, 2))
                ])

        box_distance.sort(key=lambda x: x[1])

        # Computing circuits
        # Each box starts in its own circuit (set with only itself)
        # In ascending order of distance, each box pair is considered
        # If the two boxes are in different circuits, the two are merged

        circuit_list = [{box[3]} for box in box_list]

        while True:
            for box in box_distance:
                box_pair, _ = box
                first_box, second_box = box_pair
                first_set = get_set(circuit_list, first_box)

                if second_box in first_set:
                    continue

                second_set = get_set(circuit_list, second_box)
                circuit_list.remove(first_set)
                circuit_list.remove(second_set)
                circuit_list.append(first_set.union(second_set))

                if len(circuit_list) == 1:
                    first_x = [x[0] for x in box_list if x[3] == first_box][0]
                    second_x = [x[0] for x in box_list if x[3] == second_box][0]

                    return first_x * second_x


p2 = Part_2()
p2.test(25272)
p2.execute()
