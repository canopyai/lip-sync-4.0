import numpy as np
from scipy.interpolate import interp1d
from scipy.ndimage import gaussian_filter1d

def interpolate_with_cumulative_easing(data, num_extra_points=2, sigma=1):
    """
    Adds extra points around each original point for smoothing.

    Args:
        data (list of dicts): Original data.
        num_extra_points (int): Number of extra points to add around each original point.
        sigma (float): Standard deviation for Gaussian kernel.

    Returns:
        list of dicts: Data with smoothed target values.
    """
    cumulative_durations = np.cumsum([item['duration'] for item in data])
    targets = [item['targets'] for item in data]

    smoothed_data = []

    # Function to generate extra points around each original point
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

    for i in range(len(targets[0])):
        target_values = [target[i] for target in targets]
        extra_x, extra_y = generate_extra_points(cumulative_durations, target_values, num_extra_points)
        smoothed_values = gaussian_filter1d(extra_y, sigma=sigma)

        # Update smoothed values back into data
        for j, item in enumerate(smoothed_data):
            item['targets'][i] = smoothed_values[j]

    # Recalculate durations from cumulative durations
    new_cumulative_durations = [extra_x[0]] + list(np.diff(extra_x))
    for j in range(len(smoothed_data)):
        smoothed_data[j]['duration'] = new_cumulative_durations[j]

    return smoothed_data
