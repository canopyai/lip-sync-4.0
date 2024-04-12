# Define the function to add weight property to each phoneme dict
from process_syllables.syllables_data import lip_heavy_consonant
def add_weight(phoneme_dicts):
    
    
    for phoneme_dict in phoneme_dicts:
        # Initialize weight with default value
        phoneme_dict['weight'] = 1
        
        # Add weight for lip-heavy consonants
        if phoneme_dict['base'] in lip_heavy_consonant:
            phoneme_dict['weight'] += 2.5
        
        # Add weight for stress of 1
        if phoneme_dict['stress'] == 1:
            phoneme_dict['weight'] += 1
    
    return phoneme_dicts

