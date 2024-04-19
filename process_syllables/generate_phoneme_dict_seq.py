from process_syllables.add_weight import add_weight
from process_syllables.implement_combos import implement_combos
from process_syllables.modify_vowels_and_consonants_stress import modify_vowels_and_consonants_stress
from process_syllables.obfuscate_modifiers import obfuscate_modifiers
from process_syllables.transform_to_objects_with_properties import transform_to_objects_with_properties


def generate_phoneme_dict_seq (phoneme_list):
  phoneme_list = implement_combos(phoneme_list)

  phoneme_dicts = transform_to_objects_with_properties(phoneme_list)


  phoneme_dicts = modify_vowels_and_consonants_stress(phoneme_dicts)
  phoneme_dicts = obfuscate_modifiers(phoneme_dicts)
  phoneme_dicts = add_weight(phoneme_dicts)
  return phoneme_dicts
  # lets remove modifiers
