# models.py
from django.db import models

class TextInput(models.Model):
    text = models.CharField(max_length=50)

    class Meta:
        db_table = 'textinputting'
