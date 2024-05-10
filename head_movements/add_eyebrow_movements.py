import random
from head_movements.get_eyebrow_selection_movement import get_eyebrow_selection_movement


def add_eyebrow_movements(int_alvs, emotion):
    if len(int_alvs) > 3:
        print(f'There are {len(int_alvs)} dicts')
        startIndex = random.randint(1, 2) if len(int_alvs) > 4 else 0
        endIndex = len(int_alvs) - 1 if random.choice([True, False]) else len(int_alvs) - 2
        strength = random.uniform(0.5, 1)

        # Iterate through the list and modify the targets based on the defined indices
        for index, alv in enumerate(int_alvs):
            if index < startIndex:
                # Extend with zeros if before the start index
                alv['targets'].extend([0, 0, 0, 0])
            elif startIndex <= index <= endIndex:
                # Get movement adjustments based on emotion, adjust by strength, and extend
                adjustments = get_eyebrow_selection_movement(emotion)
                alv['targets'].extend([x * strength for x in adjustments])
            else:
                # Extend with zeros if after the end index
                alv['targets'].extend([0, 0, 0, 0])



        print(f'Start index: {startIndex}, End index: {endIndex}, Strength: {strength}')
    else:
        # If the list is not long enough, extend all with zeros
        print("Not enough data to perform eyebrow movements, extending with zeros.")
        for alv in int_alvs:
            alv['targets'].extend([0, 0, 0, 0])

    return int_alvs