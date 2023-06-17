from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CipherText(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    key = models.CharField(max_length=100, null=True, blank=True)
    algo_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} --> {self.title}'

