from django.db import models
from datetime import datetime

# Create your models here.

class CoinFlip(models.Model):
    CHOICES = (('H', 'Head'), ('T', 'Tail'))
    side = models.CharField(choices=CHOICES, max_length=1)
    datetime: datetime = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_last_flips(n: int):
        result = CoinFlip.objects.order_by('-datetime')
        return result[:n]

    def __str__(self):
        return f"Сторона: {self.side}<br> Дата{self.datetime.strftime('%d-%m-%Y, %H:%M:%S')} {type(self.datetime)}"
