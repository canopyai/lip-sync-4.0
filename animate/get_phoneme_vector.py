from animate.viseme_key import viseme_key

def get_phoneme_vector(phoneme_dict):
    
    #get base vector
    stress_value = phoneme_dict["stress"]
    key_value = phoneme_dict["base"]

    stress_index = 0
    if stress_value == 1:
        stress_index = 1


    base_viseme_index = viseme_key[key_value][str(stress_index)]
    
    # construct base vector
    base_vector = [0]*37
    base_vector[base_viseme_index-1] = 1

    #get modifier vector
    modifier_vector = [0]*37
    for modifier in phoneme_dict["modifiers"]:
        modifier_index = viseme_key[modifier][str(stress_index)]
        modifier_vector[modifier_index-1] = 1

    #combine vectors
    combined_vector = [0]*37
    for i in range(37):
        combined_vector[i] = base_vector[i] + modifier_vector[i]
    
    return combined_vector
