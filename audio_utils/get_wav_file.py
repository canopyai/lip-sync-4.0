import requests
import base64
from audio_utils.resample_audio import resample_audio
import base64
import time

api_url = 'http://35.234.101.2:8080/api/v1/static'
first_chunk_url  = 'http://34.91.134.10:8080/api/v1/static'


def get_wav_file(text, isFirstChunk):

    data = {
        'text': text,
        'voice': "m-us-3", 
        'steps': 13, 
        'alpha': 0.3,
        'beta': 0.7,
        'speed': 0.8, 
        "embedding_scale":1, 
        # "speed":0.8

    }

    print("Getting audio file", text)

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

    print("time to unpack b64 + audio file", time.time() - startTime)

    return audio_base64


