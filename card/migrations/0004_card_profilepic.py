# Generated by Django 3.2.3 on 2021-10-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_rename_cards_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Profile Pic'),
        ),
    ]
