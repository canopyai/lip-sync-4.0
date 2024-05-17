import numpy as np
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d

def add_smoothing_points(data, num_extra_points=2, sigma=1):
    """
    Adds extra points around each original point for smoothing.

    Args:
        data (list of dicts): Original data.
        num_extra_points (int): Number of extra points to add around each original point.
        sigma (float): Standard deviation for Gaussian kernel.

    Returns:
        list of dicts: Data with smoothed target values.
    """
    durations = [item['duration'] for item in data]
    cumulative_durations = np.cumsum(durations)
    targets = [item['targets'] for item in data]

    new_data = []

    def generate_extra_points(x, y, num_extra_points):
        new_x = []
        new_y = []
        for i in range(len(x) - 1):
            x_interp = np.linspace(x[i], x[i + 1], num=num_extra_points + 2)
            y_interp = interp1d(x, y, kind='linear')(x_interp)
            new_x.extend(x_interp[:-1])
            new_y.extend(y_interp[:-1])
        new_x.append(x[-1])
        new_y.append(y[-1])
        return new_x, new_y

    # Generating extra points for each target
    for i in range(len(targets[0])):
        target_values = [target[i] for target in targets]
        extra_x, extra_y = generate_extra_points(cumulative_durations, target_values, num_extra_points)
        smoothed_values = gaussian_filter1d(extra_y, sigma=sigma)
        
        if i == 0:
            # Initialize the new data structure
            for j in range(len(smoothed_values)):
                new_data.append({'duration': 0, 'targets': [0] * len(targets[0])})
        
        # Update targets with smoothed values
        for j in range(len(smoothed_values)):
            new_data[j]['targets'][i] = smoothed_values[j]

    # Calculate new durations
    for j in range(1, len(new_data)):
        new_data[j]['duration'] = extra_x[j] - extra_x[j - 1]

    return new_data

