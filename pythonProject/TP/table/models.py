from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    column1 = models.CharField(max_length=255)
    column2 = models.CharField(max_length=255)
    column3 = models.CharField(max_length=255)
    user = models.ManyToManyField(User)

    def __str__(self):
       return f'{self.column1}{self.column2}{self.column3}{self.user}'