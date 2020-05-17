from django.urls import path
from .views import *

app_name = "breadapp"

urlpatterns = [
    path('', bread_list, name='bread_list'),
    path('bread/form', bread_form, name='bread_form'),
    path('bread/<int:bread_id>/', bread_details, name='bread_details'),
    path('bread/<int:bread_id>/form/', bread_edit_form, name='bread_edit_form'),
]
