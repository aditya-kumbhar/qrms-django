from django import forms

class StudLoginForm(forms.Form):
    username = forms.TextInput()
    password = forms.PasswordInput()
    