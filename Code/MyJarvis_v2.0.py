import speech_recognition as sr
from gtts import gTTS
import os

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Start Speaking!! the model will automatically detect the end of the speech as it encounters long pause...")
    audio=r.listen(source)

try:
    eng_conv= r.recognize_google(audio, language = "en-US")
    bong_conv= r.recognize_google(audio, language = "bn-IN")
    hin_conv= r.recognize_google(audio, language = "hi-IN")
    kan_conv= r.recognize_google(audio, language = "kn-IN")
   
    print("In English:   " + eng_conv)
    tts = gTTS(text=eng_conv, lang='en-US')
    tts.save("eng.mp3")
    os.system("mpg321 eng.mp3")
    print("In Bengali:   " + bong_conv)
    tts = gTTS(text=eng_conv, lang='bn')
    tts.save("eng.mp3")
    os.system("mpg321 eng.mp3")
    print("In Kannada: "+ kan_conv)
    #tts = gTTS(text=eng_conv, lang='kn')
    #tts.save("eng.mp3")
    #os.system("mpg321 eng.mp3")
    print("In Hindi: "+hin_conv)
    tts = gTTS(text=eng_conv, lang='hi')
    tts.save("eng.mp3")
    os.system("mpg321 eng.mp3")
except sr.UnknownValueError:
    print("Audio Unknown (or not understood)")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


