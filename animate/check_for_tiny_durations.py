def check_for_tiny_durations(list):
    # Iterate through each element in the list
    for item in list[0]:
        # Check if the duration of the current element is less than 0.03
        if item['duration'] < 50:
            # If found, return True
            return True
    # If the loop completes without finding any duration less than 0.03, return False
    return False