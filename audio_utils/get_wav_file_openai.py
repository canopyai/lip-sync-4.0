from openai import OpenAI
from pathlib import Path
import openai
import base64


client = OpenAI(
)


def get_wav_file(text_segment):
    speech_file_path = Path(__file__).parent / "speech.wav"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text_segment,
        response_format="wav"
    )
    response.stream_to_file(speech_file_path)

    with open(speech_file_path, "rb") as file:
        wav_data = file.read()
        base64_wav = base64.b64encode(wav_data).decode("utf-8")

    return base64_wav
