from process_syllables.syllables_data import lip_heavy_consonant

def modify_vowels_and_consonants_stress(phoneme_dicts):

    
    for i in range(len(phoneme_dicts) - 1):  # Iterate through the list, excluding the last element
        current_phoneme = phoneme_dicts[i]
        
        if current_phoneme['base'] in lip_heavy_consonant:
            next_phoneme_dict = phoneme_dicts[i]
            # Check if the next phoneme is a vowel with a stress
            if next_phoneme_dict['stress'] is not None:
                if next_phoneme_dict['stress'] == 1:
                    # If original vowel stress was 1, set it to 0 and set the consonant's stress to 1
                    next_phoneme_dict['stress'] = 0
                    current_phoneme['stress'] = 1
                else:
                    # For stress 0 or 2, keep the original stresses but reflect them on both consonant and vowel
                    current_phoneme['stress'] = next_phoneme_dict['stress']
    
    return phoneme_dicts
