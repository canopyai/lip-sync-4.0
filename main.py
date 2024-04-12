from animate.generate_word_viseme_dict import generate_word_viseme_dict
from audio_utils.get_wav_file import get_wav_file
from audio_utils.resample_audio import resample_audio
from phonemize.get_segments_torch import get_segments
from utils.unpack_nested_list import unpack_nested_list
from animate.remove_mid_word_sils import remove_mid_word_sils

from flask_cors import CORS
import pandas as pd
from flask import Flask, request





app = Flask(__name__)
CORS(app)

@app.route('/generate_animation', methods=['GET'])
def main():
    url = request.url
    query_params = request.args.to_dict()
    sentence = query_params["text"]
    b64string = get_wav_file(sentence)
    raw_wav_file = "audio_utils/speech.wav"
    resampled_wav_file = "audio_utils/resampled.wav"
    resample_audio(raw_wav_file, resampled_wav_file)

    segments = get_segments(resampled_wav_file, sentence)
    print(segments)
   
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
        
        print(word, duration, internal_word_duration)
        
        animation_sequence_packed.append(generated_word_viseme_dict)

    print("duration_step_1_summer", duration_step_1_summer)

    unpacked_animation_sequence = unpack_nested_list(animation_sequence_packed)



    summed = sum([item['duration'] for item in unpacked_animation_sequence])
    
    return {"visemes": unpacked_animation_sequence, "b64string": b64string}



# main()

# main(sentence)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")