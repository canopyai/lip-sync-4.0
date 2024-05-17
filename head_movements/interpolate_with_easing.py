import numpy as np
from scipy.interpolate import interp1d

def interpolate_with_cumulative_easing(data, interval=15):
    # Calculate cumulative durations excluding the first segment
    cumulative_durations = [0] + [sum(entry['duration'] for entry in data[:i+1]) for i in range(1, len(data))]
    
    # Number of deltas
    num_deltas = len(data[0]['targets'])
    
    # Prepare new list
    new_data = [{'duration': data[0]['duration'], 'targets': data[0]['targets']}]
    
    # Generate interpolated points for each delta index
    for i in range(num_deltas):
        x = cumulative_durations[1:]
        y = [entry['targets'][i] for entry in data][1:]
        f = interp1d(x, y, kind='cubic')
        x_new = np.arange(x[0], x[-1], interval)
        y_new = f(x_new)
        
        # Create new entries for each interpolated point
        for j in range(len(x_new)):
            if j >= len(new_data) - 1:
                new_data.append({'duration': interval, 'targets': [0] * num_deltas})
            new_data[j + 1]['targets'][i] = y_new[j]
    
    return new_data
