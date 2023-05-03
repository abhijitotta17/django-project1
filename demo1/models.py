from django.db import models
# Create your models here.
class ModelStudent(models.Model):
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    email= models.EmailField( max_length=254)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name