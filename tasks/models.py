from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    Priority_choices = [  # nested List, where it contains tuples
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()  # for large amounts of text
    priority = models.CharField(max_length=1, choices=Priority_choices, default='M')
    due_date = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)


# How tasks should be displayed in Django Admin interface

def _str_(self):
    return self.title

# Create database table for the models: `python manage.py makemigrations`
# Followed by `python manage.py migrate`
