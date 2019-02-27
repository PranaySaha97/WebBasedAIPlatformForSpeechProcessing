from django import forms

class ChoiceForm(forms.Form):
    ch = forms.CharField(max_length = 100)

class SpeechRecogForm (forms.Form):
    textSpace = forms.CharField(widget= forms.Textarea)