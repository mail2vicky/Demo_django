from django.db import models

# Create your models here.
class student(models.Model):

    # s_id = models.AutoField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    # image = models.ImageField()
    file= models.FileField()



class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

class car(models.Model):
    name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)


    def __str__(self) -> str:
        return self.name 
    