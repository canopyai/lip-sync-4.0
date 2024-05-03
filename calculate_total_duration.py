def calculate_total_duration(segments):
    # Initialize total duration to zero
    total_duration = 0.0
    
    # Iterate over each segment in the list
    for segment in segments:
        # Add the duration from each segment to the total duration
        total_duration += segment['duration']
    
    # Return the total duration
    return total_duration