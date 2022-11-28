from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    username = models.CharField(max_length=20, help_text="Entre com o nickname", primary_key=True)
    email = models.EmailField(help_text="Informe o Email", max_length=254)

class EasyScore(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    score = models.IntegerField(default=0, null=False, blank=False)

class NormalScore(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    score = models.IntegerField(default=0, null=False, blank=False)

class HardScore(models.Model):
    username = models.CharField(max_length=20, blank=False, null=False)
    score = models.IntegerField(default=0, null=False, blank=False)

class EasyScore2(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, null=False, blank=False)

class NormalScore2(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, null=False, blank=False)

class HardScore2(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0, null=False, blank=False)




