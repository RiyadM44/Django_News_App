# models.py
from django.db import models

class TextInput(models.Model):
    # Auto-incrementing primary key
    ID = models.AutoField(primary_key=True)
    # Field for text input
    text_input = models.CharField(max_length=50)
    # Field for image input
    # image = models.ImageField(upload_to='static/', default='dbeaver.png')
    image = models.ImageField(upload_to='static/')

    class Meta:
        # Specify the table name
        db_table = 'textinputting'

# class NewsData(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     image_url = models.URLField()
#     news_url = models.URLField()

#     def __str__(self):
#         return self.title

#     class Meta:
#         # Specify the table name
#         db_table = 'newsDataTable'

