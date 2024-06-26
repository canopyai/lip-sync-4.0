import librosa
import soundfile as sf

def resample_audio(input_wav_path, output_wav_path, target_sr=16000):

    audio, original_sample_rate = librosa.load(input_wav_path, sr=None)

    # Resample the audio to 16k Hz.
    resampled_audio = librosa.resample(audio, orig_sr=original_sample_rate, target_sr=target_sr)

    # Save the resampled audio to a new WAV file.
    sf.write(output_wav_path, resampled_audio, target_sr)