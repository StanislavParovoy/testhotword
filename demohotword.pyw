import os
import struct
import sys
from datetime import datetime
import numpy as np
import pyaudio
import soundfile
from porcupine import Porcupine
from util import *
import speech_recognition as sr

r = sr.Recognizer()

def listenmic():
    num_keywords = 1
    print('Ждем ключевого слова roxy:')
    porcupine = None
    pa = None
    audio_stream = None
    try:
        porcupine = Porcupine(library_path='lib/libpv_porcupine.dll', model_file_path='lib/porcupine_params.pv', keyword_file_paths=['keywords/americano_windows.ppn'], sensitivities=[0.5])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length, input_device_index=None)
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm)
            if num_keywords == 1 and result:
                
                print('Слушаю')
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    print(r.recognize_google(audio, language="ru-RU"))
                    print('Ждем ключевого слова roxy:')
                except sr.UnknownValueError:
                    print("Робот не расслышал фразу")
                    print('Ждем ключевого слова roxy:')
                except sr.RequestError as e:
                    print("Ошибка сервиса; {0}".format(e))
                    
    finally:
        if porcupine is not None: porcupine.delete()
        if audio_stream is not None: audio_stream.close()
        if pa is not None: pa.terminate()
    _AUDIO_DEVICE_INFO_KEYS = ['index', 'name', 'defaultSampleRate', 'maxInputChannels']


listenmic()

