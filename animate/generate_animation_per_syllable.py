from animate.get_phoneme_vector import get_phoneme_vector
def generate_animation_per_syllable(phoneme_list, duration):
    vectorised_phoneme_list = []
    total_syllable_weight = 0
    for phoneme_dict in phoneme_list:
        total_syllable_weight += phoneme_dict["weight"]

    for phoneme in phoneme_list:
        phoneme_data = {}
        phoneme_data["duration"] = (phoneme["weight"]/total_syllable_weight)*duration
        phoneme_data["targets"] = get_phoneme_vector(phoneme)
        phoneme_data["base"] = phoneme["base"]
        vectorised_phoneme_list.append(phoneme_data)

    # lets remove modifiers
    return vectorised_phoneme_list