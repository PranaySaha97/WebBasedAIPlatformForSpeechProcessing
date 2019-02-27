from django.shortcuts import render
from UI.form import ChoiceForm
from UI.form import SpeechRecogForm
from django.http import HttpResponse
import speech_recognition as sr
import webbrowser
from textblob import TextBlob
import matplotlib.pyplot as plt
import os
import datetime
import pyttsx3

# Create your views here.

def index(request):
    return render(request, "UI/index.html")


def about(request):
    return render(request, "UI/about.html")


def contact(request):
    return render(request, "UI/contact.html")

def menu(request):
    if request.method=='POST':
        choiceForm= ChoiceForm(request.POST)

        if choiceForm.is_valid():
            choice = choiceForm.cleaned_data['ch']
        else:
            choiceForm= ChoiceForm()
        choice = int(choice)
        if choice==1:
            return render(request, "UI/speech_recog.html")
        elif choice==2:
            return render(request, "UI/speech_synth.html")
        elif choice==3:
            return render(request,"UI/speech_trans.html")
        elif choice==4:
            return render(request,"UI/speech_auth.html")
        elif choice==5:
            return render(request,"UI/speech_analy.html")
        elif choice==6:
            return render(request,"UI/speech_cmd.html")
        else:
            return HttpResponse("<script><alert>Invalid Choice</alert></script>")


def speech_recog(request):

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")

    try:
        t=r.recognize_google(audio)
        print(t)
        return render(request, 'UI/speech_recog.html', {'t': t})
    except sr.UnknownValueError:
        t="Audio Unknown (or not understood)"
        return render(request, 'UI/speech_recog.html', {'t': t})
    except sr.RequestError as e:
        t="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, 'UI/speech_recog.html', {'t': t})


def speech_trans(request):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")

    try:
        eng_conv= r.recognize_google(audio, language = "en-US")
        bong_conv= r.recognize_google(audio, language = "bn-IN")
        hin_conv= r.recognize_google(audio, language = "hi-IN")
        kan_conv= r.recognize_google(audio, language = "kn-IN")
        print("In English:   " + eng_conv)
        print("In Bengali:   " + bong_conv)
        print("In Kannada: "+ kan_conv)
        print("In Hindi: "+hin_conv)

        return render(request, 'UI/speech_trans.html', {'eng': eng_conv,'bong':bong_conv,'hin':hin_conv,'kan':kan_conv})
    except sr.UnknownValueError:
        t="Audio Unknown (or not understood)"
        return render(request, 'UI/speech_trans.html', {'t':t})
    except sr.RequestError as e:
        t="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, 'UI/speech_trans.html', {'t':t})

def speech_auth(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")
    try:
        t=r.recognize_google(audio)
        print ("You just said " ,t)
        
        t=t.strip().lower()
        
        if t == 'sunny':
            print("Hey Sunny!! How may I help you?")
            webbrowser.open_new_tab('https://www.linkedin.com/in/7sunny-singh/')
            return render(request, 'UI/speech_auth.html')
        elif t == 'rick' or t=='unlock me':
            print("Hey Pranay!! How may I help you?")
            webbrowser.open_new_tab('https://www.linkedin.com/in/pranay-saha-42820011a/')
            return render(request, 'UI/speech_auth.html')
        else:
            t="Not authenticated"
            return render(request, 'UI/speech_auth.html', {'t':t})
    except sr.UnknownValueError:
        t="Audio Unknown (or not understood)"
        return render(request, 'UI/speech_auth.html', {'t':t})
    except sr.RequestError as e:
        t="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, 'UI/speech_auth.html', {'t':t})

        
def speech_analy(request):
    polarity = 0
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")

    try:
        t= r.recognize_google(audio, language = "en-US")
        analysis = TextBlob(t)
        polarity += analysis.sentiment.polarity
        conv="Your Statement: "+t  

        if (polarity == 0):
            emotion="Neutral"
        elif (polarity > 0 and polarity <= 0.3):
            emotion="Weakly Positive"
        elif (polarity > 0.3 and polarity <= 0.6):
            emotion="Positive"
        elif (polarity > 0.6 and polarity <= 1):
            emotion="Strongly Positive"
        elif (polarity > -0.3 and polarity <= 0):
            emotion="Weakly Negative"
        elif (polarity > -0.6 and polarity <= -0.3):
            emotion="Negative"
        elif (polarity > -1 and polarity <= -0.6):
            emotion="Strongly Negative"

        return render(request, 'UI/speech_analy.html', {'conv':conv, 'emotion':emotion})
    except sr.UnknownValueError:
        t="Audio Unknown (or not understood)"
        return render(request, 'UI/speech_analy.html', {'t':t})
    except sr.RequestError as e:
        t="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, 'UI/speech_analy.html', {'t':t})


def speech_command(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")
    try:
        t=r.recognize_google(audio)
        print ("You just said " ,t)

        t=t.strip().lower()

        if t == 'show date':
            print("Showing Date")
            os.system('date')
            msg = datetime.datetime.now()
            str(msg)
            return render(request, "UI/speech_cmd.html",{'msg':msg})
        elif t == 'show time':
            print("Showing Time")
            os.system('time')
            return render(request, "UI/speech_cmd.html")
        elif t == 'shut down':
            print('Shutting Down')
            os.system('poweroff')
            return render(request, "UI/speech_cmd.html")
        elif t == 'reboot now':
            print('Rebooting Now')
            os.system('reboot')
            return render(request, "UI/speech_cmd.html")
        elif t== 'play my favourite video':
            print('Playing your video')
            webbrowser.open('https://www.youtube.com/watch?v=UhYRlI_bpJQ')
            return render(request, "UI/speech_cmd.html")
        elif t == 'which is my college':
            print('Your college is: SJCIT')
            webbrowser.open('http://sjcit.ac.in/')
            return render(request, "UI/speech_cmd.html")
        else:
            msg="Command Not Recognised Yet!! Please Try Again"
            return render(request, "UI/speech_cmd.html",{'msg':msg})

            
    except sr.UnknownValueError:
        msg="Audio Unknown (or not understood)"
        return render(request, "UI/speech_cmd.html",{'msg':msg})
    except sr.RequestError as e:
        msg="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, "UI/speech_cmd.html",{'msg':msg})


def speech_synthesis(request):
    voiceEngine = pyttsx3.init()
    r=sr.Recognizer()
    voiceEngine.setProperty('rate', 150)
    voiceEngine.setProperty('volume', 0.8)
    with sr.Microphone() as source:
        print ("A moment of silence")
        r.adjust_for_ambient_noise(source, duration = 1)
        print("Say something!")
        audio = r.listen(source)
        print("Trying to recognize audio")

    try:
        t=r.recognize_google(audio)
        msg="You said "+t
        voiceEngine.say(msg)
        voiceEngine.runAndWait()
        print(msg)
        return render(request, 'UI/speech_synth.html', {'msg': msg})
    except sr.UnknownValueError:
        t="Audio Unknown (or not understood)"
        return render(request, 'UI/speech_synth.html', {'msg': t})
    except sr.RequestError as e:
        t="Could not request results from Google Speech Recognition service; {0}".format(e)
        return render(request, 'UI/speech_synth.html', {'msg': t})

