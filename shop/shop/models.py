from django.db import models

class User(models.Model):
    fname = models.CharField(max_length=128)
    lname = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.fname
