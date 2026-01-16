from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout


def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
# Create your views here.
