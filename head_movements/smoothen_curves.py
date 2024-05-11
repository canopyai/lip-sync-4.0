import numpy as np

def ease_in_out(t):
    """Cubic ease-in-ease-out function."""
    return 3 * t**2 - 2 * t**3

def sine_half_wave(t):
    """Sine half-wave function that decays to zero."""
    return np.sin(np.pi * t)

def smoothen_curves(animations, step_duration=15):
    new_animations = []
    for i in range(len(animations) - 1):
        initial_targets = animations[i]['targets']
        final_targets = animations[i + 1]['targets']
        total_duration = animations[i]['duration']
        steps = total_duration // step_duration

        # Calculate the interpolated targets for each step, applying sine half-wave
        for step in range(steps + 1):
            t = step / steps
            eased_t = ease_in_out(t)
            sine_wave_modulation = sine_half_wave(t)
            interpolated_targets = [(initial + (final - initial) * eased_t) * sine_wave_modulation for initial, final in zip(initial_targets, final_targets)]
            new_animations.append({'duration': step_duration, 'targets': interpolated_targets})

    return new_animations

