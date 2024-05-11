import numpy as np

def ease_in_out(t):
    """Cubic ease-in-ease-out function."""
    return 3 * t**2 - 2 * t**3

def smoothen_curves(animations, step_duration=15, decay_steps=10):
    new_animations = []
    for i in range(len(animations) - 1):
        initial_targets = animations[i]['targets']
        final_targets = animations[i + 1]['targets']
        total_duration = animations[i]['duration']
        steps = total_duration // step_duration

        # Calculate the interpolated targets for each step
        for step in range(steps + 1):
            t = step / steps
            eased_t = ease_in_out(t)
            interpolated_targets = [initial + (final - initial) * eased_t for initial, final in zip(initial_targets, final_targets)]

            # Apply decay to the last 10 elements of each sequence
            if step >= steps - decay_steps + 1:
                decay_factor = (steps - step) / decay_steps
                interpolated_targets = [target * decay_factor for target in interpolated_targets]

            new_animations.append({'duration': step_duration, 'targets': interpolated_targets})

    return new_animations