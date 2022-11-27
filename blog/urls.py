from django.urls import path
from .views import *
app_name = "blog"
urlpatterns = [
    path('index/' , index , name="index") ,
    path('post/<slug:slug>/' , post , name="post"),
]