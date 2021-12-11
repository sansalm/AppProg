from django.db import models
from django.contrib.auth.models import User

class Games(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Details(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    text = models.TextField()
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."
