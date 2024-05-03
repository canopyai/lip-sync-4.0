import numpy as np

tick_duration = 0.25
shape_std_dev_scalar = 0.5
def create_gaussian_shape_array(sampled_point, shape_std_dev, duration, tick_duration):
    num_samples = int(duration / tick_duration)  # Calculate the number of points to generate
    gaussian_array = np.zeros(num_samples)  # Initialize the array with zeros
    
    # Populate the array with values from a Gaussian function
    for i in range(num_samples):
        x = i * tick_duration
        # Gaussian formula: exp(-(x - b)^2 / (2 * c^2)), b is mean (sampled_point here), c is std_dev
        gaussian_array[i] = np.exp(-(x - sampled_point)**2 / (2*shape_std_dev_scalar * shape_std_dev**2))
    
    return gaussian_array

def generate_smoothing_array(smoothing, duration, tick_duration):
    num_samples = int(duration / tick_duration)  # Calculate the number of points to generate
    
    if smoothing == -1:
        # Generate values from 0 to pi/2 and apply sine to transition from 0 to 1
        x_values = np.linspace(0, np.pi/2, num_samples)
        smoothing_array = np.sin(x_values)
    
    elif smoothing == +1:
        # Generate values from pi/2 to 0 and apply sine to transition from 1 to 0
        x_values = np.linspace(np.pi/2, 0, num_samples)
        smoothing_array = np.sin(x_values)
    
    elif smoothing == 0:
        # Return an array of ones if smoothing is 0
        smoothing_array = np.ones(num_samples)
    
    else:
        # Optional: Handle other smoothing values or return an empty array
        smoothing_array = np.array([])  # Return an empty array or handle other cases as needed
    
    return smoothing_array

def generate_emotion_sequence(duration, smoothing):
    mean = duration / 2
    sampling_std_dev = duration/5

    sampled_point = np.random.normal(loc=mean, scale=sampling_std_dev)
    sampled_point = max(0, min(sampled_point, duration))
    sampled_point = sampled_point + (duration- sampled_point) * np.random.uniform(0, 1)
    gaussian_shape_array = create_gaussian_shape_array(sampled_point, 2, duration, tick_duration)
    smoothing_array = generate_smoothing_array(smoothing, duration, tick_duration)

    # Apply the smoothing envelope to the Gaussian shape array
    smoothed_gaussian_array = gaussian_shape_array * smoothing_array

    return smoothed_gaussian_array

def transform_lists(list_of_lists):
    # Calculate the number of elements in the smallest list to ensure uniformity
    min_length = min(len(lst) for lst in list_of_lists)
    
    # Prepare the result list
    result = []
    
    # Loop through each index up to the minimum length
    for i in range(min_length):
        # Extract the ith element from each list and create a new list of these elements
        new_list = [lst[i] for lst in list_of_lists if len(lst) > i]
        
        # Attach this list to an object with a 'targets' key and a 'duration' property
        obj = {'targets': new_list, 'duration': tick_duration*1000}
        
        # Append this object to the result list
        result.append(obj)
    
    return result

def generate_emotion_sequences (emotion_vector, duration, smoothing=0):
    # Initialize the list to store the Gaussian shape arrays
    gaussian_shape_arrays = []
    
    # Generate the Gaussian shape array for each emotion in the emotion vector
    for i, emotion in enumerate(emotion_vector):
        # Generate the Gaussian shape array for the emotion
        gaussian_shape = generate_emotion_sequence(duration, smoothing) * emotion
        # Append the Gaussian shape array to the list
        gaussian_shape_arrays.append(gaussian_shape.tolist())
    
    return transform_lists(gaussian_shape_arrays)


# # Example usage:
emotion_vector = [1, 0, 0, 0]  # Example vector, not used in this specific implementation
duration = 5  # Duration of the emotional expression or event
gaussian_shape = generate_emotion_sequences(emotion_vector,duration, 1)
