from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="mainpage"),
    path("redirect",views.redirect,name="redirect")
]