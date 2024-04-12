modifiers = ["S", "Z", "L", "T", "D", "N", "NG", ]

def obfuscate_modifiers(phoneme_dicts):
    updated_phoneme_dicts = []
    i = 0
    while i < len(phoneme_dicts):
        current_dict = phoneme_dicts[i]
        
        if current_dict['base'] in modifiers:
            # Modifier found, check for adjacent vowels
            if i > 0 and 'stress' in phoneme_dicts[i - 1] and phoneme_dicts[i - 1]['stress'] is not None:
                # Previous phoneme is a vowel, add current modifier to its list
                phoneme_dicts[i - 1]['modifiers'].append(current_dict['base'])
            if i < len(phoneme_dicts) - 1 and 'stress' in phoneme_dicts[i + 1] and phoneme_dicts[i + 1]['stress'] is not None:
                # Next phoneme is a vowel, add current modifier to its list
                phoneme_dicts[i + 1]['modifiers'].append(current_dict['base'])
            # Skip adding the current_dict to updated_phoneme_dicts as it's removed
        else:
            # Current phoneme is not a modifier, add it to the list
            updated_phoneme_dicts.append(current_dict)
        
        i += 1  # Move to the next phoneme
    
    return updated_phoneme_dicts