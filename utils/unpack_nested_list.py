def unpack_nested_list(list_of_lists):
    unpacked_list = []
    # Iterate through each sublist in the list of lists
    for sublist in list_of_lists:
        # Iterate through each dictionary in the sublist
        for dictionary in sublist:
            # Add the dictionary to the unpacked_list
            unpacked_list.append(dictionary)
    return unpacked_list
