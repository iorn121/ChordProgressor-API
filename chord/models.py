from django.db import models


class Tone(models.Model):
    order = models.IntegerField(verbose_name="順番")
    key = models.IntegerField(verbose_name="基音")
    octave = models.IntegerField(verbose_name="オクターブ")
    chord = models.IntegerField(verbose_name="和音")
    length = models.IntegerField(verbose_name="長さ")
