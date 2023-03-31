from django.db import models

# Create your models here.
'''model to display the contact detail of school'''
class contactlist(models.Model):
    address=models.TextField(max_length=900, blank=False)
    email=models.CharField(max_length=100, blank=False)
    phone=models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.email

'''model to get the inquery form details'''
class contactform(models.Model):
    name=models.CharField(max_length=100, blank=False)
    email=models.CharField(max_length=100, blank=False)
    subject=models.CharField(max_length=100, blank=False)
    message=models.TextField(max_length=800, blank=False)

    def __str__(self):
        return self.name