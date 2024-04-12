def split_phonemes(phonemes):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    split_list_dicts = []
    current_island = []

    for phoneme in phonemes:
        # Check if current phoneme is a vowel
        is_vowel_phoneme = phoneme[0] in vowels
        # Extract vowel stress, defaulting to '0' for consonants
        vowel_stress = phoneme[-1] if phoneme[-1].isdigit() else '0'
        
        if current_island:
            # If types differ or both are vowels (to ensure only one vowel per island), conclude current island
            if is_vowel_phoneme != current_island[0]['is_vowel'] or is_vowel_phoneme:
                # Append current island as dictionary
                split_list_dicts.append({
                    'phoneme_list': [ph['phoneme'] for ph in current_island],
                    'vowel_stress': current_island[0]['vowel_stress'],
                    'is_vowel': current_island[0]['is_vowel']
                })
                # Reset current island with the new phoneme
                current_island = [{
                    'phoneme': phoneme,
                    'vowel_stress': vowel_stress,
                    'is_vowel': is_vowel_phoneme
                }]
            else:
                # For consonants, continue adding to the current island
                current_island.append({
                    'phoneme': phoneme,
                    'vowel_stress': vowel_stress,
                    'is_vowel': is_vowel_phoneme
                })
        else:
            # Start the first island with the first phoneme
            current_island.append({
                'phoneme': phoneme,
                'vowel_stress': vowel_stress,
                'is_vowel': is_vowel_phoneme
            })

    # Add the last island to the list if not empty
    if current_island:
        split_list_dicts.append({
            'phoneme_list': [ph['phoneme'] for ph in current_island],
            'vowel_stress': current_island[0]['vowel_stress'],
            'is_vowel': current_island[0]['is_vowel']
        })

    return split_list_dicts
