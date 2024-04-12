from graphemes.convert_word_to_graphemes import convert_word_to_graphemes
from graphemes.split_phonemes import split_phonemes
from graphemes.merge_phonemes import merge_phonemes_according_to_rules
from process_syllables.generate_phoneme_dict_seq import generate_phoneme_dict_seq
from animate.generate_animation_per_syllable import generate_animation_per_syllable
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_useless_phonemes import remove_useless_phonemes


from animate.remove_tiny_durations import remove_tiny_durations

def generate_word_viseme_dict(word, duration):
    #step 1 graphemise

    word_vector_dicts = []

    structure_phonemes = ["<s>", "</s>", "<sil>"]

    if word in structure_phonemes:
        structured_phoneme_vector = [0]*37
        structured_phoneme_vector[0] = 1
        return [{"duration": duration, "targets": structured_phoneme_vector}]

    graphemes = convert_word_to_graphemes(word)

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

    


    # print(word_vector_dicts[0]["base"], word_vector_dicts[0]["duration"])
    # pre_op_acc = 0
    # for j in word_vector_dicts:
    #     for i in j:
    #         print(i["duration"], i["base"])
    #         pre_op_acc += i["duration"]

    word_vector_dicts = remove_tiny_durations(word_vector_dicts)

    # print(word_vector_dicts)
    
    # post_op_acc = 0

    # for k in word_vector_dicts:
    #     for l in k:
    #         print(l["base"], l["duration"])
    #         post_op_acc += l["duration"]
    
    # print("durations", pre_op_acc, post_op_acc)


    

    unpacked_word_vector_dicts = unpack_nested_list(word_vector_dicts)
    
    return unpacked_word_vector_dicts


    



    

        

    #step 3 generate visemes from syllable

    #rules around phonemes
    
    #before processing remove modifiers

    #r1: any vowel after a lip consonant vowel has stress 0
    #r2: modifiers only get applied to vowels concurrently with vowels
    #r3: Add weightings to timings according to required deviation of mouth shape


    return merge_graphemes
