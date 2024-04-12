def transform_to_objects_with_properties(phoneme_list):
    objects_list = []

    for phoneme in phoneme_list:
        # Initialize base, stress, and modifiers for each phoneme
        base = phoneme.rstrip('012').upper()  # Remove stress indicators and uppercase
        stress = None
        modifiers = []

        # Determine if the phoneme has a stress indicator
        if phoneme[-1] in '012':
            stress = int(phoneme[-1])

        # Append the constructed object to the list
        objects_list.append({
            'base': base,
            'stress': stress,
            'modifiers': modifiers, 
            'weight': None
        })

    return objects_list

