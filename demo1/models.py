from django.db import models
# Create your models here.
class ModelStudent(models.Model):
    regid=models.CharField(primary_key=True,max_length=20)
    name=models.CharField(max_length=20)
    marks=models.IntegerField()
    email= models.EmailField( max_length=254)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.name