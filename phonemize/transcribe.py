import sys
import json
from pocketsphinx import AudioFile
import os

def transcribe_with_timestamps(audio_path):
        segments = []
        config = {
            'verbose': False,
            'audio_file': os.path.abspath(audio_path),
            'samprate': 16000,
        }


        audio = AudioFile(**config)
        for phrase in audio:
            for segment in phrase.segments(detailed=True):
                word, log_likelihood, start_frame, end_frame = segment
                segments.append((word, start_frame, end_frame))

        return segments

if __name__ == '__main__':
    audio_path = sys.argv[1]
    segments = transcribe_with_timestamps(audio_path)