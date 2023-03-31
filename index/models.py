from django.db import models

# Create your models here.
'''
model for about page
'''
class about(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=900, blank=False)
    Image=models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title

'''
model for slider
'''
class slider(models.Model):
    title=models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=900, blank=False)
    Image=models.ImageField(upload_to='slider/', blank=False)

    def __str__(self):
        return self.title
    
class notice(models.Model):
    message=models.TextField(max_length=200,blank=True)

    def __str__(self):
        return self.message

