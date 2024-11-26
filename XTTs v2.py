import requests
from TTS.api import TTS
import os

# Download a sample speaker file
speaker_wav_path = "/content/Narendra_Modi_voice.ogg-[AudioTrimmer.com].wav"

# Initialize TTS model
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Generate speech by cloning the voice from the sample speaker
output_path = "output.wav"
tts.tts_to_file(
    text=" में मदद करते हैं",
    file_path=output_path,
    speaker_wav=speaker_wav_path,
    language="hi"
)

print(f"Speech synthesis complete! Output saved at: {output_path}")
