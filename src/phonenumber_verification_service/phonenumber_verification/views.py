from django.shortcuts import render
from django.http import HttpResponse
from .forms import PhonenumberForm


def index(request):
    return render(request,'index.html',{"form": PhonenumberForm()})