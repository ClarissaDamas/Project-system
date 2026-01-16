from django import forms
from django.contrib.auth.models import User # Model Used by UserCreationForm and Our new RegistrationForm
from django.contrib.auth.forms import UserCreationForm


class cadastrarform(UserCreationForm):
    #campos adicionais alem da funcao register do django
    email = forms.EmailField()

    # include Meta class
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]