from django import forms
from django.utils.safestring import mark_safe

PARAMETERS_CHOICES = [('1', 'Standard deviation and average value'),
                      ('2', 'Correlation')]


class ParametersForm(forms.Form):
    start_at = forms.CharField(label=mark_safe('</br>Start at'), max_length=10,
                               widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    end_at = forms.CharField(label=mark_safe('</br>End at'), max_length=10,
                             widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    choice = forms.ChoiceField(label=mark_safe('</br></br>Which parameters'), widget=forms.RadioSelect, choices=PARAMETERS_CHOICES)
    cur1 = forms.CharField(required=False, label=mark_safe('</br>Correlation - currency 1'), max_length=3,
                               widget=forms.TextInput(attrs={'placeholder': 'XXX'}))
    cur2 = forms.CharField(required=False, label=mark_safe('</br>Correlation - currency 2'), max_length=3,
                             widget=forms.TextInput(attrs={'placeholder': 'XXX'}))