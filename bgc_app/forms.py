from django import forms

from .models import Games, Details

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = ['text', 'originalowner', 'currentowner']
        labels = {'text': 'Game:', 'originalowner': 'Original owner:',
                  'currentowner': 'Current owner:'}

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['text']
        labels = {'text': 'Details:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
