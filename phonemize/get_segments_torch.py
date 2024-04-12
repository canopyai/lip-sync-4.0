import torch
import torchaudio
import time
from phonemize.fa_helper.get_trellis import get_trellis
from phonemize.fa_helper.backtrack import backtrack
from phonemize.fa_helper.merge_repeats import merge_repeats
from phonemize.fa_helper.merge_words import merge_words
from phonemize.fa_helper.process_words import process_words

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
torch.random.manual_seed(0)
bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
model = bundle.get_model().to(device)
labels = bundle.get_labels()


def get_segments(speech_file, text):
    transcript = "|" + "|".join(text.upper().split()) + "|"
    startTime = time.time()
    with torch.inference_mode():
        waveform, _ = torchaudio.load(speech_file)   
        emissions, _ = model(waveform.to(device))
        emissions = torch.log_softmax(emissions, dim=-1)
    emission = emissions[0].cpu().detach()
    # transcript = "|I|HAD|THAT|CURIOSITY|BESIDE|ME|AT|THIS|MOMENT|"
    dictionary = {c: i for i, c in enumerate(labels)}
    tokens = [dictionary[c] for c in transcript]
    trellis = get_trellis(emission, tokens)
    path = backtrack(trellis, emission, tokens)
    segments = merge_repeats(path, transcript)
    words = merge_words(segments)
    ratio = waveform[0].size(0) / bundle.sample_rate / trellis.size(0)
    words = process_words(words, ratio)
    print(f"Elapsed time: {time.time() - startTime:.2f} s")
    return words


