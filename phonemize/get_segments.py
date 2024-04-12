import subprocess
import json
import re
from phonemize.format_phonemes import format_phonemes
from phonemize.convert_word_to_graphemes import convert_word_to_graphemes

def get_segments (filename):
    language_env_name = "python3"
    result = subprocess.run([language_env_name, 'phonemize/transcribe.py', filename], capture_output=True, text=True)
    segments = json.loads(result.stdout)
    segments = format_phonemes(segments)

    results = []
    for segment in segments:
        word = segment['word']
        word = re.sub(r'\([^)]*\)', '', word).strip()

        start = segment['start_time']
        end = segment['end_time']
        graphemes = convert_word_to_graphemes(word)
        results.append({
            'word': word,
            'start': start,
            'end': end,
            'graphemes': graphemes
        })
    return results