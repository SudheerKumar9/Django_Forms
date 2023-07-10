from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *


def djforms(request):
    SUFO=SignUpForm()
    d={'SUFO':SUFO}

    if request.method=='POST':
        SUFDT=SignUpForm(request.POST)
        if SUFDT.is_valid():
            name=SUFDT.cleaned_data['name']
            age=SUFDT.cleaned_data['age']
            email=SUFDT.cleaned_data['email']
            password=SUFDT.cleaned_data['password']
            gender=SUFDT.cleaned_data['gender']
            courses=SUFDT.cleaned_data['courses']
            return HttpResponse('<center><h1>Data is collected From Back End</h1></center>')

    return render(request,'djforms.html',d)