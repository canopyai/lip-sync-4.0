def remove_mid_word_sils(phoneme_dicts):
    special_characters = set('!@#$%^&*()_+=-[]{};:\'",<.>/?\\|`~')
    
    def is_valid_phoneme(phoneme):
        return all(c.isalnum() or c.isspace() for c in phoneme) and not all(c.isspace() for c in phoneme)

    for phoneme_dict in phoneme_dicts:
        phoneme_dict['graphemes'] = [phoneme for phoneme in phoneme_dict['graphemes'] if is_valid_phoneme(phoneme) and phoneme.strip() not in special_characters]

    sil_indexes = [i for i, entry in enumerate(phoneme_dicts) if entry['word'] == '<sil>']
    
    for index in reversed(sil_indexes): 
        if index > 0: 
            phoneme_dicts[index - 1]['end'] = phoneme_dicts[index]['end']
            
        if index + 1 < len(phoneme_dicts):  # If there is a next word
            phoneme_dicts[index + 1]['start'] = min(phoneme_dicts[index]['start'], phoneme_dicts[index + 1]['start'])
        
        # Remove the <sil> entry
        phoneme_dicts.pop(index)
    
    return phoneme_dicts


