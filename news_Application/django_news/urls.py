# helloapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('save-text-input/', save_text_input, name='save_text_input'),
]
