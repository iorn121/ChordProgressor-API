from django.db import models
from django.contrib.postgres.fields import ArrayField

class Tone(models.Model):
    name = models.CharField(max_length=255,verbose_name="コード名")
    key = models.IntegerField(verbose_name="基音")
    octave = models.IntegerField(verbose_name="オクターブ")
    chord = models.CharField(max_length=255,verbose_name="和音")
    length = models.CharField(max_length=255,verbose_name="長さ")

    def __title__(self):
        return self.name
