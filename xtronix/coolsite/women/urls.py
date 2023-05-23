from django.urls import path

from .views import *

urlpatterns = [
        path('', index), #  http://10.1.201.58:8000/women/ 
        path('cats/', categories) #  http://10.1.201.58:8000/women/cats
        ]
