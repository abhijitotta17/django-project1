from django import forms


class NameForm(forms.Form):
    Username = forms.CharField(label="Your name", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    password=forms.CharField(label="Your Password" , max_length=100, widget=forms.TextInput(attrs={'placeholder':'Enter your password'}))