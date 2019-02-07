#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:00:25 2018

@author: pranay
"""

import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)

try:
	print("Google Speech Recognition thinks you said in English: -  " + r.recognize_google(audio, language = "en-US"))
	print("Google Speech Recognition thinks you said in Bengali: -  " + r.recognize_google(audio, language = "bn-IN"))
    print(r.recognize_google(audio,language="kn-IN"))
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
	print("Could not request results from Google Speech Recognition service; {0}".format(e))