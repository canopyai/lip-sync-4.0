import re
import copy
import bisect

import bisect

def find_pair_punctuation(text):
    all_pairs = []
    text = text.replace("'", "")  # Remove all apostrophes
    punctuations = [',', '.', '!', '?', ':', ';', '"']
    texts = text.split()  # This also handles multiple spaces correctly
    for i, text in enumerate(texts):
        if text and text[-1] in punctuations and i < len(texts) - 1:  # Check if text is not empty and last char is a punctuation
            all_pairs.append((remove_non_alphanumeric(text).upper(), remove_non_alphanumeric(texts[i + 1]).upper()))
    return all_pairs


def remove_non_alphanumeric(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text)
    return cleaned_text

def find_boundaries(tuples, dicts):
    result = []
    word_times = {}
    for d in dicts:
        if d['word'] in word_times:
            word_times[d['word']].append((d['start'], d['end']))
        else:
            word_times[d['word']] = [(d['start'], d['end'])]

    for first_word, second_word in tuples:
        if first_word in word_times and second_word in word_times:
            for f_times in word_times[first_word]:
                for s_times in word_times[second_word]:
                    if s_times[0] - f_times[1] > 65:
                        result.append((first_word, second_word))
                        break 

    return result



def handle_pauses(shapes, ided_tuples):
    updated_shapes = copy.deepcopy(shapes)
    
    def find_shape(word):
        return next((item for item in shapes if item['word'] == word), None)
    
    # Function to find the correct index to insert a new viseme while keeping the list sorted by 'start' time
    def find_insert_index(shapes, new_shape):
        starts = [shape['start'] for shape in shapes]
        return bisect.bisect(starts, new_shape['start'])

    for first_word, second_word in ided_tuples:
        first_shape = find_shape(first_word)
        second_shape = find_shape(second_word)
        
        if first_shape and second_shape:
            duration_diff = second_shape['start'] - first_shape['end']

        if(duration_diff > 99):
            neu_viseme = {
                'word': 'DEF',
                'start': first_shape['end'],
                'end': first_shape['end']+60,
                'graphemes': ['DEF'],
            }
            neu_viseme_2 = {
                'word': 'DEF',
                'start': first_shape['end']+30,
                'end': second_shape['start'],
                'graphemes': ['DEF'],
            }
            insert_index = find_insert_index(updated_shapes, neu_viseme)
            updated_shapes.insert(insert_index, neu_viseme_2)
            updated_shapes.insert(insert_index, neu_viseme)


     

    return updated_shapes


def process_handle_pause(segments, sentence):
    word_tuples = find_pair_punctuation(sentence)
    boundaries = find_boundaries(word_tuples, segments)
    handled_pauses = handle_pauses(segments, boundaries)
    return handled_pauses
