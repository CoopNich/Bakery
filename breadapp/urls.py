from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bread_list, name='bread_list'),
    path('bread/form', bread_form, name='bread_form'),
]
