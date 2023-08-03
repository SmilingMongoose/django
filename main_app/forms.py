from django import forms

class BasicInput(forms.Form):
    visitor_name = forms.CharField(max_length=200)