from django.shortcuts import render
from . import calorieapi
# Create your views here.

def index(request):
    return render(request,'content/index.html')

def content(request):
    if request.method=="POST":
        r1 = calorieapi.GetNutrition(request.POST.get("item"))
        return render(request,'content/data.html', {
            'cal' : r1["items"][0]["calories"]
        })
