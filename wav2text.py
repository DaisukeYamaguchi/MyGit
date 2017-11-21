# -*- coding: utf-8 -*-
import speech_recognition

def get_text(file):
    r = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(file) as source:
        audio = r.record(source)
    
    return r.recognize_google(audio, language='ja-JP')

