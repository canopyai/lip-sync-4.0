import eventlet
eventlet.monkey_patch()

from animate.generate_word_viseme_dict import generate_word_viseme_dict
from audio_utils.get_wav_file import get_wav_file
from audio_utils.resample_audio import resample_audio
from phonemize.get_segments_torch import get_segments
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_mid_word_sils import remove_mid_word_sils

from flask_cors import CORS
import pandas as pd
from flask import Flask, request
import time
import base64
import re








app = Flask(__name__)
CORS(app)

@app.route('/generate_animation', methods=['POST'])
def main():
    data = request.get_json()
    sentence = data["text"]
    isFirstChunk = data["isFirstChunk"]
    preWav = time.time()
    b64string = get_wav_file(sentence, isFirstChunk)
    raw_wav_file = "audio_utils/speech.wav"
    resampled_wav_file = "audio_utils/resampled.wav"
    resampled_wav_file_22 = "audio_utils/22050_res.wav"
    mid_wav_time = time.time()
    resample_audio(raw_wav_file, resampled_wav_file, 16000)
    resample_audio(raw_wav_file, resampled_wav_file_22, 22050)
    postWav = time.time()

    print(f'Time to resample audio: {postWav - mid_wav_time}')


    sentence = re.sub(r'[^A-Z]', '', sentence.upper())


    segments, segments_latency = get_segments(resampled_wav_file, sentence)

    segments = remove_mid_word_sils(segments)

    animation_sequence_packed = []
    duration_step_1_summer = 0

    # Initialize last_end_time with the start time of the first segment for the initial duration calculation
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

    print("duration_step_1_summer", duration_step_1_summer)

    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)


    print("duration_step_1_summer", duration_step_1_summer)

    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)

    last_dict = unpacked_animation_sequence[-1]

    summed = sum([item['duration'] for item in unpacked_animation_sequence])


    with open(resampled_wav_file_22, 'rb') as file:
        wav_binary_data = file.read()

    # Encode the binary data to a Base64 string
    b64_encoded_data = base64.b64encode(wav_binary_data)

    # Convert Base64 bytes to string for easier handling/display
    b64_22 = b64_encoded_data.decode('utf-8')
     
    return {"visemes": unpacked_animation_sequence, "b64string": b64_22, "segments_latency": segments_latency, "tts_latency":postWav - preWav}



# main()

# main(sentence)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")