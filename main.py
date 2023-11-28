import requests
from api_02 import *

filename = "output.wav"
audio_url = upload(filename)



save_transcript(audio_url, 'file')