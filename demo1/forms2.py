from django import forms
from demo1.models import ModelStudent
class studentFeom(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name'}))
    marks=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter your mark'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your number'}))
    '''name=forms.CharField()
    marks=forms.IntegerField()'''
    class Meta:
        model=ModelStudent
        fields='__all__'

