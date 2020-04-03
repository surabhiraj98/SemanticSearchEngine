from typing import Any, Union

from django.shortcuts import render
from .models import MyUser
import sys
from subprocess import run, PIPE, CompletedProcess


def searchView(request):
    data=request.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'Form1.html',{'data':data})
def external(request):
    inp=request.POST.get('raj')out = run([sys.executable,'C:\Users\HP\Python\main.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request, 'home.html', {'data1': out.stdout})



def registerView(request):
        user=myUser(request.POST)
        user.save()
         render(request,'Form3.html',{'data':data})
def button(request):
  render(request,'Form3.html')
