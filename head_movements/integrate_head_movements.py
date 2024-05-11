def integrate_head_movements(alvs, previousHeadMovementsStarting):
    # Starting position
    current_position = previousHeadMovementsStarting["previousHeadMovementsStarting"]
    # List to store the movement information with positions
    movement_info = []

    # Iterate over each set of deltas and duration
    for movement in alvs:
        deltas = movement['deltas']
        duration = movement['duration']
        # Update current_position by adding the corresponding deltas
        current_position = [current_pos + delta for current_pos, delta in zip(current_position, deltas)]
        previousHeadMovementsStarting["previousHeadMovementsStarting"] = current_position
        # Append the new position and duration to the list
        movement_info.append({'duration': duration, 'targets': current_position.copy()})
    
    return movement_info