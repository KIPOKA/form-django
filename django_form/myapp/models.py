from django.db import models

# Create your models here.


class Snippet(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=90)

    def __str__(self):
        return self.name
