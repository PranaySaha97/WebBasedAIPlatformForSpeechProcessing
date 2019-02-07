import speech_recognition as sr


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
    print("In Bengali:   " + bong_conv)
    print("In Kannada: "+ kan_conv)
    print("In Hindi: "+hin_conv)
except sr.UnknownValueError:
    print("Audio Unknown (or not understood)")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


