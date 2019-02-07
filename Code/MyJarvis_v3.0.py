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
    
    eng_conv=eng_conv.strip().lower()
    
    if eng_conv == 'james':
        print("Hey Sunny!! How may I help you?")
        '''tts = gTTS(text="Hey Sunny!! How may I help you?", lang='en')
        tts.save("eng.mp3")
        os.system("mpg321 eng.mp3")'''
    elif eng_conv == 'hey tony':
        print("Hey Pranay!! How may I help you?")
    else:
        print("Not authenticated")
   

    print("In English:   " + eng_conv)
    '''print("In Bengali:   " + bong_conv)
    print("In Kannada: "+ kan_conv)
    print("In Hindi: "+hin_conv)'''
except sr.UnknownValueError:
    print("Audio Unknown (or not understood)")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


