from django.shortcuts import render
def index(request):
    return render(request,"mainpage/main.html",{})

def redirect(request):
    if request.method=='POST':
        redirect("")
from django.shortcuts import redirect


# Create your views here.