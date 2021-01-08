from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    naziv = models.CharField(max_length=50)
    ocena = models.IntegerField(max_length=10)
    godina = models.IntegerField()
    kreiraoJe = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.naziv

    #python manage.py makemigrations
    #python manage.py migrate