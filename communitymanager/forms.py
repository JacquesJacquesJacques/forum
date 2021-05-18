from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="User name", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
