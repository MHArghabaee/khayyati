# Generated by Django 5.1.3 on 2024-11-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khayyat', '0007_remove_order_fabric_length1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='تاریخ تحویل'),
        ),
        migrations.AlterField(
            model_name='order',
            name='deposit',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='بیعانه(تومان)'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fabric',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='مشخصات پارچه'),
        ),
        migrations.AlterField(
            model_name='order',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pants',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='مشخصات شلوار'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='order',
            name='wage',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='اجرت(تومان)'),
        ),
    ]
