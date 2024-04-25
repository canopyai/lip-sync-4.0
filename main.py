from animate.generate_word_viseme_dict import generate_word_viseme_dict
from audio_utils.get_wav_file import get_wav_file
from audio_utils.resample_audio import resample_audio
from phonemize.get_segments_torch import get_segments
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_mid_word_sils import remove_mid_word_sils
from pydantic import BaseModel
from fastapi import FastAPI

class AnimationRequest(BaseModel):
    text: str

import pandas as pd

import time
app = FastAPI()

@app.post('/generate_animation')
async def main(request: AnimationRequest):
    sentence = request.text
    preWav = time.time()
    b64string = get_wav_file(sentence)
    raw_wav_file = "audio_utils/speech.wav"
    resampled_wav_file = "audio_utils/resampled.wav"
    resample_audio(raw_wav_file, resampled_wav_file)
    postWav = time.time()
    sentence = sentence.replace(".", "").replace(",", "").replace("!", "").replace("?", "").upper()

    segments, segments_latency = get_segments(resampled_wav_file, sentence)

    segments = remove_mid_word_sils(segments)

    animation_sequence_packed = []
    duration_step_1_summer = 0
    if segments:
        last_end_time = segments[0]['start']

    for segment in segments:
        word = segment['word']
        
        duration = segment['end'] - last_end_time
        last_end_time = segment['end']
        
        duration_step_1_summer += duration
        generated_word_viseme_dict = generate_word_viseme_dict(word, duration)
        internal_word_duration = 0
        for gwv in generated_word_viseme_dict:
            internal_word_duration += gwv['duration']

        animation_sequence_packed.append(generated_word_viseme_dict)

    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)


    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)
    
    return {"visemes": unpacked_animation_sequence, "b64string": b64string, "segments_latency": segments_latency, "tts_latency":postWav - preWav}


