def remove_useless_phonemes(phoneme_dicts):
    # Define the list of phonemes considered useless
    useless_phonemes = ['K', 'G', "Y", "H", "HH"]
    
    # Iterate through each dictionary in the input list
    for phoneme_dict in phoneme_dicts:
        # Filter out useless phonemes from the phoneme_list
        phoneme_dict['phoneme_list'] = [phoneme for phoneme in phoneme_dict['phoneme_list'] if phoneme not in useless_phonemes]
    
    return phoneme_dicts
