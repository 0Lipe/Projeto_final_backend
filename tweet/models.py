from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=280)  

    def __str__(self):
        return f"{self.user.username}: {self.tweet}"
