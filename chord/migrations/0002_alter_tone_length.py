# Generated by Django 4.0.4 on 2022-05-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chord', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tone',
            name='length',
            field=models.CharField(max_length=255, verbose_name='長さ'),
        ),
    ]
