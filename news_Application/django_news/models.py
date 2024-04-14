# models.py
from django.db import models

class CarouselImage(models.Model):
    ID = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='carousel_images')

    class Meta:
        db_table = 'carousel_images'


# class TextInput(models.Model):
#     # Auto-incrementing primary key
#     ID = models.AutoField(primary_key=True)
#     text_input = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='static/')

#     class Meta:
#         # Specify the table name
#         db_table = 'textinputting'

