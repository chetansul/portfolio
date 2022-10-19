from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    subject = models.TextField(max_length=300, null=True)
    message = models.TextField()


def __str__(self):
    return self.name
