from django import forms

class Urlform(forms.Form):
    form_url_field = forms.URLField(label="enter url", required=True,widget=forms.TextInput(attrs={'placeholder': 'Shorten your link'}))