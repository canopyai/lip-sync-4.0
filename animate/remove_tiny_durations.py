from animate.check_for_tiny_durations import check_for_tiny_durations
from animate.remove_shortest_duration import remove_shortest_durations

def remove_tiny_durations(nested_list):
    while check_for_tiny_durations(nested_list):
        nested_list = remove_shortest_durations(nested_list)
    return nested_list