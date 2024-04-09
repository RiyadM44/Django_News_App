from django.db import models

class TextInput(models.Model):
    # Auto-incrementing primary key
    ID = models.AutoField(primary_key=True)
    # Field for text input
    text_input = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/')

    class Meta:
        # Specify the table name
        db_table = 'textinputting'
