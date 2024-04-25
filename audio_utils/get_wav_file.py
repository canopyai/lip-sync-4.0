import requests
import base64
from audio_utils.resample_audio import resample_audio
import base64

api_url = 'http://35.234.101.2:8080/api/v1/static'


def get_wav_file(text):

    data = {
        'text': text,
        'voice': "m-us-3", 
        'steps': 13, 
        'alpha': 0.3,
        'beta': 0.7,
        'speed': 0.8, 
        "embedding_scale":1
    }

    print("Getting audio file", text)


    response = requests.post(api_url, json=data)
    audio_base64 = response.json()['audio_base64']

    # Decode the base64 string to audio data
    audio_data = base64.b64decode(audio_base64)

    # Write the audio data to a WAV file
    with open('speech.wav', 'wb') as file:
        file.write(audio_data)

    return audio_base64


