from django import forms
from .models import *


class infoform(forms.ModelForm):
    class Meta:
        model=info
        fields='__all__'


class noteform(forms.ModelForm):
    class Meta:
        model=note
        fields='__all__'



class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'