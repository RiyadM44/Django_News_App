# forms.py
from django import forms
from .models import CarouselImage

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = CarouselImage
        fields = ['image']

# class TextInputForm(forms.ModelForm):
#     class Meta:
#         model = TextInput
#         fields = ['text_input']

# class NewsDataForm(forms.ModelForm):
#     class Meta:
#         model = NewsData
#         fields = ['title', 'description', 'image_url', 'news_url']
