from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_image = models.ImageField(upload_to='skill_app')

    def __str__(self):
        return self.name
