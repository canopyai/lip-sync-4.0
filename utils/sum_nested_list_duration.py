def sum_nested_list_structure(nested_list):
    flat_list = nested_list[0]
    duration_acc = 0
    for item in flat_list:
        duration_acc += item['duration']
    return duration_acc