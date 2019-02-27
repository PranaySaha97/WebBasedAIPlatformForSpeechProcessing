from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('menu/', views.menu, name="menu"),
    path('speech_recognition/', views.speech_recog, name="SpeechRecognition"),
    path('speech_translation/', views.speech_trans, name="SpeechTranslation"),
    path('speech_authentication/', views.speech_auth, name="SpeechAuthentication"),
    path('speech_analysis/', views.speech_analy, name="SpeechAnalysis"),
    path('speech_command/', views.speech_command, name="SpeechCommand"),
    path('speech_synthesis/', views.speech_synthesis, name="SpeechSynth"),

]
