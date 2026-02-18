from django.db import models


class Contact(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.EmailField()


class Social(models.Model):
    title = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100,blank=True)
    address = models.TextField()
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='socials',
    )

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return f"{self.email}"
