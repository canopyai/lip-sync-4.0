def format_phonemes(segments):
    words_list = []
    frame_rate_multiplier = 1000/(100)

    for segment in segments:
        word, start_frame, end_frame = segment 


        start_time = start_frame * frame_rate_multiplier
        end_time = end_frame * frame_rate_multiplier

        phoneme_object = {
            'word': word,
            'start_time': start_time,
            'end_time': end_time
        }
        words_list.append(phoneme_object)

    return words_list