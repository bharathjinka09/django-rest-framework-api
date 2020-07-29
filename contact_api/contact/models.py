from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.first_name + '-' + self.last_name
