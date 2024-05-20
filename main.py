import eventlet
eventlet.monkey_patch()

from animate.generate_word_viseme_dict import generate_word_viseme_dict
from audio_utils.get_wav_file import get_wav_file
from audio_utils.resample_audio import resample_audio
from phonemize.get_segments_torch import get_segments
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_mid_word_sils import remove_mid_word_sils
# from emotions.generate_emotion_sequences import generate_emotion_sequences
from get_duration import get_wav_duration
from calculate_total_duration import calculate_total_duration
from deduplicate_visemes import deduplicate_visemes
from implementRR import implementRR
from process_syllables.process_handle_pause import process_handle_pause
from head_movements.orchestrate_head_movement_curves import orchestrate_head_movement_curves


from flask_cors import CORS
import pandas as pd
from flask import Flask, request 
import time
import base64
import re
import os



app = Flask(__name__)
CORS(app)



@app.route('/generate_animation', methods=['POST'])
def main():
    print("Request received")
    start_time = time.time() 
    data = request.get_json()
    sentence = data["text"]
    isFirstChunk = data["isFirstChunk"]
    add_post_padding = data["add_post_padding"]
    voice_vector = data["voice_vector"]
    speed = data["speed"]
    preWav = time.time()
    b64string = get_wav_file(sentence, isFirstChunk, voice_vector, speed)
    print(f'Wav file generated: {time.time() - preWav:.2f}s')
    raw_wav_file = "audio_utils/speech.wav"
    resampled_wav_file = "audio_utils/resampled.wav"
    resampled_wav_file_22 = "audio_utils/22050_res.wav"
    resample_audio(raw_wav_file, resampled_wav_file, 16000)
    resample_audio(raw_wav_file, resampled_wav_file_22, 22050)
    duration = get_wav_duration(resampled_wav_file)

    postWav = time.time()
    original_sentence = sentence
    sentence = re.sub(r'[^A-Z\s]', '', sentence.upper())
    segments, segments_latency = get_segments(resampled_wav_file, sentence)
    print(f'Segments generated: {time.time() - postWav:.2f}s')

    head_movement_curves, int_alvs_brows = orchestrate_head_movement_curves(segments)
    segments = remove_mid_word_sils(segments)

    segments = implementRR(segments)
    segments = process_handle_pause(segments, original_sentence)


    animation_sequence_packed = []
    duration_step_1_summer = 0

    f_dict  = None
    if segments:
        last_end_time = segments[0]['start']

        f_dur = last_end_time
        f_structured_phoneme_vector = [0]*37
        f_structured_phoneme_vector[0] = 1
        f_dict =  [{"duration": f_dur, "targets": f_structured_phoneme_vector}]

    previous_targets = None
    for segment in segments:
        word = segment['word']
        
        duration = segment['end'] - last_end_time
        last_end_time = segment['end']
        
        duration_step_1_summer += duration

        generated_word_viseme_dict = generate_word_viseme_dict(word, duration, segment["graphemes"], previous_targets)
        if(len(generated_word_viseme_dict) > 0):
            previous_targets = generated_word_viseme_dict[-1]["targets"]

        internal_word_duration = 0
        for gwv in generated_word_viseme_dict:
            internal_word_duration += gwv['duration']

        animation_sequence_packed.append(generated_word_viseme_dict)
    
    animation_sequence_packed.append(f_dict)



    if add_post_padding:
        g_structured_phoneme_vector = [0]*37
        g_structured_phoneme_vector[0] = 1
        g_dict =  [{"duration": 600, "targets": g_structured_phoneme_vector}]
        animation_sequence_packed.append(g_dict)




    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)
    
    # gms = generate_emotion_sequences(emotion_vector, duration_step_1_summer/1000, 0)

    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)

    unpacked_animation_sequence = deduplicate_visemes(unpacked_animation_sequence)

    with open(resampled_wav_file_22, 'rb') as file:
        wav_binary_data = file.read()

    # Encode the binary data to a Base64 string
    b64_encoded_data = base64.b64encode(wav_binary_data)

    # Convert Base64 bytes to string for easier handling/display
    b64_22 = b64_encoded_data.decode('utf-8')

    tot = calculate_total_duration(unpacked_animation_sequence)

    end_time = time.time()

    print(f'Duration: {end_time - start_time:.2f}s')
     
    return {
        "visemes": unpacked_animation_sequence, 
        ""
        "b64string": b64_22, 
        "segments_latency": segments_latency, 
        "tts_latency":postWav - preWav,
        "head_movement_curves": head_movement_curves, 
        "int_alvs_brows":int_alvs_brows
        # "emotion_sequences":gms
        }



# main()

# main(sentence)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")