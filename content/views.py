from django.shortcuts import render
from . import calorieapi
# Create your views here.

def index(request):
    return render(request,'content/index.html')

def content(request):
    if request.method=="POST":
        breakfList = calorieapi.GetNutrition(request.POST.get("bfield"))
        LunchList = calorieapi.GetNutrition(request.POST.get("lfield"))
        dinnList = calorieapi.GetNutrition(request.POST.get("dfield"))
        miscList = calorieapi.GetNutrition(request.POST.get("mfield"))
        return render(request,'content/data.html', {
            #'cal' : r1["items"][0]["calories"]
            
        })
