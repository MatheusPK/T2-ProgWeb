from django.db import models

# Create your models here.

class Player(models.Model):
    nickname = models.CharField(max_length=20, help_text="Entre com o nickname", primary_key=True)
    email = models.EmailField(help_text="Informe o Email", max_length=254)

    def __str__(self) -> str:
        return self.nickname

class Score(models.Model):
    DIFFICULTIES = (
        (u'E', u'EASY'),
        (u'M', u'NORMAL'),
        (u'H', u'HARD')
    )
    nickname = models.ForeignKey(Player, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTIES)
    score = models.IntegerField(default=0)

    def __str__(self) -> str:
        return (self.nickname, self.difficulty)

