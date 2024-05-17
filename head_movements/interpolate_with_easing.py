import numpy as np
from scipy.interpolate import interp1d

def interpolate_with_cumulative_easing(data, interval=15):
    cumulative_durations = [sum(entry['duration'] for entry in data[:i+1]) for i in range(len(data))]
    
    # Number of deltas
    num_deltas = len(data[0]['targets'])
    
    # Prepare new list
    new_data = []
    
    # Generate interpolated points for each delta index
    for i in range(num_deltas):
        x = cumulative_durations
        y = [entry['targets'][i] for entry in data]
        f = interp1d(x, y, kind='cubic')
        x_new = np.arange(x[0], x[-1], interval)
        y_new = f(x_new)
        
        # Create new entries for each interpolated point
        for j in range(len(x_new)):
            if j >= len(new_data):
                new_data.append({'duration': interval, 'targets': [0] * num_deltas})
            new_data[j]['targets'][i] = y_new[j]
    
    return new_data
