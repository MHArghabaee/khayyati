# Generated by Django 5.1.3 on 2024-11-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khayyat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='شماره تلفن'),
        ),
    ]