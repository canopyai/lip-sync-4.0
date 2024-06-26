import requests
import base64
from audio_utils.resample_audio import resample_audio
import base64
import time

api_url = 'http://34.32.129.161:8080/api/v1/static'
first_chunk_url  = 'http://34.34.2.18:8080/api/v1/static'


def get_wav_file(text, isFirstChunk, voice_vector=[1, 0, 0], speed=0.9):
    rev_alpha = 0.3
    rev_beta = 0.7
    if(voice_vector[2] == 1):
        rev_alpha = 0
        rev_beta = 0
        print("Voice vector is 2")
    
    data = {
        'text': text, 
        'voice': voice_vector,
        'steps': 20,
        'alpha': rev_alpha,
        'beta': rev_beta,
        'speed': speed,
        "embedding_scale":1,

        # "speed":0.8

    }


    url_to_use = api_url

    if isFirstChunk:
        url_to_use = first_chunk_url
        


    response = requests.post(url_to_use, json=data)

    startTime = time.time()
    audio_base64 = response.json()['audio_base64']

    # Decode the base64 string to audio data
    audio_data = base64.b64decode(audio_base64)

    # Write the audio data to a WAV file
    with open('audio_utils/speech.wav', 'wb') as file:
        file.write(audio_data)


    return audio_base64


