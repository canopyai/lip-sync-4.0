from graphemes.convert_word_to_graphemes import convert_word_to_graphemes
from graphemes.split_phonemes import split_phonemes
from graphemes.merge_phonemes import merge_phonemes_according_to_rules
from process_syllables.generate_phoneme_dict_seq import generate_phoneme_dict_seq
from animate.generate_animation_per_syllable import generate_animation_per_syllable
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_useless_phonemes import remove_useless_phonemes


from animate.remove_tiny_durations import remove_tiny_durations

def generate_word_viseme_dict(word, duration, graphemes):

    print("Generating word viseme dict for word: ", word, " with duration: ", duration, " and graphemes: ", graphemes)

    word_vector_dicts = []

    structure_phonemes = ["<s>", "</s>", "<sil>"]

    if word in structure_phonemes:
        structured_phoneme_vector = [0]*37
        structured_phoneme_vector[0] = 1
        return [{"duration": duration, "targets": structured_phoneme_vector}]

    split_graphemes = split_phonemes(graphemes)

    merge_graphemes = merge_phonemes_according_to_rules(split_graphemes)

    merge_graphemes  = remove_useless_phonemes(merge_graphemes)

    



    accumulate_weight_per_word = 0
    for grapheme in merge_graphemes:
        phoneme_list_per_syllable = generate_phoneme_dict_seq(grapheme["phoneme_list"])
        accumulate_weight_per_syllable = 0
        for phoneme_dict in phoneme_list_per_syllable:
            accumulate_weight_per_syllable += phoneme_dict["weight"]
        

        accumulate_weight_per_word += (accumulate_weight_per_syllable**0.5)

    for grapheme in merge_graphemes:
        phoneme_list_per_syllable = generate_phoneme_dict_seq(grapheme["phoneme_list"])
        accumulate_weight_per_syllable = 0
        for phoneme_dict in phoneme_list_per_syllable:
            accumulate_weight_per_syllable += phoneme_dict["weight"]
        syllable_duration = (accumulate_weight_per_syllable**0.5/accumulate_weight_per_word)*duration
        syllable_animation_phoneme_list = generate_animation_per_syllable(phoneme_list_per_syllable, syllable_duration)
        word_vector_dicts.append(syllable_animation_phoneme_list)


    word_vector_dicts = remove_tiny_durations(word_vector_dicts)


    

    unpacked_word_vector_dicts = unpack_nested_list(word_vector_dicts)
    
    return unpacked_word_vector_dicts


    