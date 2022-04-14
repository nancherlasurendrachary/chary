from django.urls import path
from deployementapp.views import demo
urlpatterns = [
     path('',demo,name="demo"),
    
]