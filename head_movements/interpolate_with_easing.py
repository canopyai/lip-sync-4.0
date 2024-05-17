import numpy as np


def cubic_ease_in_out(t):
    if t < 0.5:
        return 4 * t ** 3
    else:
        return 1 - 4 * (1 - t) ** 3

def interpolate_with_cumulative_easing(data, interval_ms=15):
    result = []
    current_values = [0] * 6  # Start values for 6 targets
    
    for index, item in enumerate(data):
        start_index = item['start']
        deltas = item['deltas']
        
        # Calculate the duration to the next transition or a default value
        if index < len(data) - 1:
            duration = data[index + 1]['start'] - start_index
        else:
            duration = 1000  # Default duration of 1000ms for the last segment
        
        num_frames = int(duration / interval_ms)
        for i in range(num_frames + 1):
            t = i / num_frames
            eased_t = cubic_ease_in_out(t)
            
            # Calculate eased deltas
            interpolated_deltas = [current_values[j] + deltas[j] * eased_t for j in range(6)]
            result.append({
                'deltas': interpolated_deltas,
                'start': start_index + i * interval_ms
            })
        
        # Update current_values to the last values of this segment
        current_values = [current_values[j] + deltas[j] for j in range(6)]
    
    return result

# We can re-run this function on your data and plot the results.
