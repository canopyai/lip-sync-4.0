import random
from head_movements.get_eyebrow_selection_movement import get_eyebrow_selection_movement


def add_eyebrow_movements(int_alvs, emotion):
    eyebrow_activate_prob = 0.7
    if (len(int_alvs) > 3) and random.random() < eyebrow_activate_prob:
        print(f'There are {len(int_alvs)} dicts')
        startIndex = random.randint(1, 2) if len(int_alvs) > 4 else 0
        endIndex = len(int_alvs) - 1 if random.choice([True, False]) else len(int_alvs) - 2
        strength = random.uniform(0.3, 0.7)

        # Iterate through the list and modify the targets based on the defined indices
        for index, alv in enumerate(int_alvs):
            alv["targets"]=[]
            if index < startIndex:
                alv['targets'].extend([0, 0, 0, 0])
            elif startIndex <= index <= endIndex:
                adjustments = get_eyebrow_selection_movement(emotion)

            else:
                alv['targets'].extend([0, 0, 0, 0])



    else:
        # If the list is not long enough, extend all with zeros
        for alv in int_alvs:
            alv["targets"]=[]
            alv['targets'].extend([0, 0, 0, 0])


    return int_alvs