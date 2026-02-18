from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)
    image= models.ImageField(upload_to='project_app/')

    def __str__(self):
        return self.title