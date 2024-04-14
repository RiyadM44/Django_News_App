# forms.py
from django import forms
import models

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = models.CarouselImage
        fields = ['image']


# class TextInputForm(forms.ModelForm):
#     class Meta:
#         model = TextInput
#         fields = ['text_input']

# class NewsDataForm(forms.ModelForm):
#     class Meta:
#         model = NewsData
#         fields = ['title', 'description', 'image_url', 'news_url']
