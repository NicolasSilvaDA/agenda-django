from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
