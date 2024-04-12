def remove_mid_word_sils(phoneme_dicts):
    # Define characters considered as special (you might want to expand this list)
    special_characters = set('!@#$%^&*()_+=-[]{};:\'",<.>/?\\|`~')
    
    # Function to determine if a phoneme is valid (not a special character or just space)
    def is_valid_phoneme(phoneme):
        return all(c.isalnum() or c.isspace() for c in phoneme) and not all(c.isspace() for c in phoneme)

    # Clean phoneme_lists
    for phoneme_dict in phoneme_dicts:
        print(phoneme_dict)
        phoneme_dict['graphemes'] = [phoneme for phoneme in phoneme_dict['graphemes'] if is_valid_phoneme(phoneme) and phoneme.strip() not in special_characters]

    # Find indexes of entries where the word is '<sil>'
    sil_indexes = [i for i, entry in enumerate(phoneme_dicts) if entry['word'] == '<sil>']
    
    for index in reversed(sil_indexes):  # Reverse to avoid index shift issues during removal
        if index > 0:  # If there is a previous word
            # Set the end time of the previous word to that of the <sil>
            phoneme_dicts[index - 1]['end'] = phoneme_dicts[index]['end']
            
        if index + 1 < len(phoneme_dicts):  # If there is a next word
            # Set the start time of the next word to that of the <sil>, if possible
            phoneme_dicts[index + 1]['start'] = min(phoneme_dicts[index]['start'], phoneme_dicts[index + 1]['start'])
        
        # Remove the <sil> entry
        phoneme_dicts.pop(index)
    
    return phoneme_dicts


