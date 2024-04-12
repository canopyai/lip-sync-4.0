from graphemes.convert_word_to_graphemes import convert_word_to_graphemes

def process_words(segments, ratio):
    results = []
    for segment in segments:
        # Convert start and end times using ratio and convert to milliseconds
        start_ms = int(segment.start * ratio * 1000)
        end_ms = int(segment.end * ratio * 1000)
        
        results.append({
            'word': segment.label,
            'start': start_ms,
            'end': end_ms,
            'graphemes': convert_word_to_graphemes(segment.label),
        })
    return results