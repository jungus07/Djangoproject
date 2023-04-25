from django.db import models
from django.contrib.auth.models import AbstractUser

class 아이디(AbstractUser):
    pass

# Create your models here.
class Sale(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)


    def __str__(self):
        return self.회원.username
