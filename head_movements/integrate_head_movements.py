def integrate_head_movements(alvs):
    # Starting position
    current_position = [0, 0, 0, 0, 0, 0]
    # List to store the movement information with positions
    movement_info = []

    # Iterate over each set of deltas and duration
    for movement in alvs:
        deltas = movement['deltas']
        duration = movement['duration']
        # Update current_position by adding the corresponding deltas
        current_position = [current_pos + delta for current_pos, delta in zip(current_position, deltas)]
        # Append the new position and duration to the list
        movement_info.append({'duration': duration, 'targets': current_position.copy()})
    movement_info.append({'duration': 100, 'targets': [0, 0, 0, 0, 0, 0]})
    
    return movement_info