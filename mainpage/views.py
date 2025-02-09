from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
def index(request):
        return render(request,"mainpage/main.html",{})

def redirect(request):
    if request.method=='POST':
        return HttpResponseRedirect(reverse("content:index"))



# Create your views here.