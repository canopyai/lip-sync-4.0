import requests
import base64
from audio_utils.resample_audio import resample_audio

api_url = 'http://34.141.243.146:8080/api/v1/static'
ping_url = 'http://34.141.243.146:8080/ping'


    # Parameters to send to the API


def get_wav_file(text):

    data = {
    'text': text,
    'voice': "fast-list", 
    'steps': 10, 
    'alpha': 0.3,
    'beta': 0.7,
    'speed': 0.9, 
    "embedding_scale":1
}

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        with open(f'unsamp_speech.wav', 'wb') as f:
            f.write(response.content)
    else:
        print("Error:", response.json()['error'])

    resample_audio('unsamp_speech.wav', 'speech.wav')

    with open('speech.wav', "rb") as file:
        wav_data = file.read()
        base64_wav = base64.b64encode(wav_data).decode("utf-8")

    return base64_wav


