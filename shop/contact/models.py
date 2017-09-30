from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=128)
    contact_email = models.EmailField(unique=True)
    contact_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    message = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.contact_name