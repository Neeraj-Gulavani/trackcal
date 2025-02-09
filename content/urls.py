from django.urls import path
from . import views
app_name = 'content'
urlpatterns = [
    path("",views.index,name="index"),
    path("data",views.content,name="data")
]