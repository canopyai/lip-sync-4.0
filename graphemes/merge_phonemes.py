def merge_phonemes_according_to_rules(phoneme_dicts):
    # This function assumes phoneme_dicts is already in the desired format with 'phoneme_list', 'vowel_stress', 'is_vowel'
    merged_phonemes = []
    i = 0

    while i < len(phoneme_dicts):
        current_dict = phoneme_dicts[i]

        if current_dict['is_vowel']:
            # Simply add vowel groups to the merged list
            merged_phonemes.append(current_dict)
        else:
            # Handle consonant groups
            # Determine the neighboring vowel groups
            prev_vowel_group = merged_phonemes[-1] if merged_phonemes and merged_phonemes[-1]['is_vowel'] else None
            next_vowel_group = phoneme_dicts[i + 1] if i + 1 < len(phoneme_dicts) and phoneme_dicts[i + 1]['is_vowel'] else None

            if prev_vowel_group and not next_vowel_group:
                # Vowel group only before, add consonant phonemes to the end of the previous vowel group
                prev_vowel_group['phoneme_list'].extend(current_dict['phoneme_list'])
            elif not prev_vowel_group and next_vowel_group:
                # Vowel group only after, add consonant phonemes to the start of the next vowel group
                next_vowel_group['phoneme_list'] = current_dict['phoneme_list'] + next_vowel_group['phoneme_list']
                # Skip adding the next vowel group later
                i += 1
                merged_phonemes.append(next_vowel_group)
            elif prev_vowel_group and next_vowel_group:
                # Vowel groups before and after
                if prev_vowel_group['vowel_stress'] >= next_vowel_group['vowel_stress']:
                    # Add to the end of the previous group if stress is equal or greater
                    prev_vowel_group['phoneme_list'].extend(current_dict['phoneme_list'])
                else:
                    # Add to the start of the next group
                    next_vowel_group['phoneme_list'] = current_dict['phoneme_list'] + next_vowel_group['phoneme_list']
                    # Skip adding the next vowel group later
                    i += 1
                    merged_phonemes.append(next_vowel_group)
        i += 1

    return merged_phonemes


