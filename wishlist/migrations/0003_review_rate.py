# Generated by Django 4.2.4 on 2023-09-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=2),
        ),
    ]