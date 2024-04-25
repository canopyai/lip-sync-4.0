import requests
import base64
from audio_utils.resample_audio import resample_audio

api_url = 'http://34.141.243.146:8080/api/v1/static'
ping_url = 'http://34.141.243.146:8080/ping'


    # Parameters to send to the API


def get_wav_file(text):

    data = {
        'text': text,
        'voice': "slow-emphatic", 
        'steps': 13, 
        'alpha': 0.3,
        'beta': 0.7,
        'speed': 0.8, 
        "embedding_scale":1
    }


    response = requests.post(api_url, data=data)
    audio_base64 = response.json()['audio_base64']

    return audio_base64


