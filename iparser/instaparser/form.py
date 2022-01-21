from django import forms


class UsernameForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput())
