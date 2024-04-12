combos = [("G", "R"), ("T", "R"), ("F", "R"), ("TH", "R")]
def implement_combos(phoneme_list):

    combined_phoneme_list = []
    skip_next = False

    for i, phoneme in enumerate(phoneme_list):
        if skip_next:
            skip_next = False
            continue
        if i < len(phoneme_list) - 1 and (phoneme, phoneme_list[i + 1]) in combos:
            # Combine the current and next phoneme, add to the combined list
            combined_phoneme_list.append(phoneme + phoneme_list[i + 1])
            # Set flag to skip the next phoneme since it's been combined
            skip_next = True
        else:
            # If no combination, add the phoneme as is
            combined_phoneme_list.append(phoneme)
    
    return combined_phoneme_list

