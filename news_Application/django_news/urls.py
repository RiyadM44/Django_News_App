# django_news/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.save_text_input, name='save_text_input'),
    path('index/', views.save_text_input, name='save_text_input'),
    path('news/', views.show_news, name='show_news'),
    path('upload_image/', views.upload_image, name='upload_image'),
    # path('create_news/', views.create_news, name='create_news'),
]
