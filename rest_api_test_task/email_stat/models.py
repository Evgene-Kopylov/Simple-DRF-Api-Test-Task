from django.db import models

class Letter(models.Model):
    email = models.EmailField(max_length=200)
    theme = models.CharField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.email
